// Fresh production web templates, isolated synthetic data; no store edits.
import {readFileSync,writeFileSync,mkdirSync} from 'node:fs';
const fixture=JSON.parse(readFileSync(process.env.REVIEW_WEB_FIXTURE??'build/design-agent-web-fixture.json','utf8'));
if(!/^http:\/\/127\.0\.0\.1:\d+$/.test(fixture.origin))throw new Error('Loopback fixture required');
const port=process.env.REVIEW_WEB_DEBUG_PORT??'48293';
const target=(await(await fetch(`http://127.0.0.1:${port}/json/list`)).json()).find(t=>t.type==='page');
const ws=new WebSocket(target.webSocketDebuggerUrl);await new Promise(r=>ws.addEventListener('open',r,{once:true}));
let counter=0;const pending=new Map();
ws.addEventListener('message',event=>{const v=JSON.parse(event.data);if(v.id){const p=pending.get(v.id);pending.delete(v.id);v.error?p.reject(new Error(v.error.message)):p.resolve(v.result);}});
const send=(method,params={})=>new Promise((resolve,reject)=>{const id=++counter;pending.set(id,{resolve,reject});ws.send(JSON.stringify({id,method,params}));});
const evaluate=async expression=>{const r=await send('Runtime.evaluate',{expression,awaitPromise:true,returnByValue:true});if(r.exceptionDetails)throw new Error(r.exceptionDetails.text);return r.result.value;};
await send('Page.enable');await send('Runtime.enable');
await send('Emulation.setDeviceMetricsOverride',{width:393,height:852,deviceScaleFactor:3,mobile:true});
const dir=process.env.REVIEW_WEB_OUTPUT??'build/DesignAgentReview31/raw/web';mkdirSync(dir,{recursive:true});
const screens=[];
for(const[id,key]of [['W-01-shared-wishlist','wishlist'],['W-02-gift-bag','gift'],['W-03-gift-thanks','confirmed'],['W-04-shared-stack','snap'],['W-05-bestie-invite','invite'],['W-06-private-link','private']]){
 await send('Page.navigate',{url:fixture.origin+fixture[key]});
 await evaluate("new Promise(r=>document.readyState==='complete'?r():window.addEventListener('load',r,{once:true})).then(()=>document.fonts.ready)");
 await evaluate(`Promise.all([...document.images].map(i=>{const u=new URL(i.src);if(u.origin==='https://weezy-pop-club.fly.dev'&&/^\\/s\\/[a-f0-9]{48}\\/image$/.test(u.pathname))i.src=${JSON.stringify(fixture.origin)}+u.pathname;i.loading='eager';return i.decode();})).then(()=>document.fonts.ready)`);
 const metrics=await evaluate("({width:innerWidth,documentWidth:document.documentElement.scrollWidth,height:document.documentElement.scrollHeight,prata:document.fonts.check('16px Prata'),images:[...document.images].map(i=>({loaded:i.complete&&i.naturalWidth>0}))})");
 if(metrics.width!==393||metrics.documentWidth>393||!metrics.prata||metrics.images.some(i=>!i.loaded))throw new Error(`${id}: viewport/font/image verification failed`);
 const end=Math.max(0,metrics.height-852);const offsets=[0];for(let y=742;y<end;y+=742)offsets.push(y);if(end>0)offsets.push(end);
 for(const[index,offset]of offsets.entries()){
  await evaluate(`scrollTo(0,${offset})`);await new Promise(r=>setTimeout(r,180));
  const actual=await evaluate('scrollY');
  const filename=id+(index?`-more${index>1?'-'+index:''}`:'')+'.png';
  const shot=await send('Page.captureScreenshot',{format:'png',captureBeyondViewport:false,fromSurface:true});
  writeFileSync(`${dir}/${filename}`,Buffer.from(shot.data,'base64'));
  screens.push({id:index?filename.slice(0,-4):id,parentId:index?id:undefined,filename,scrollOffset:actual,viewport:{width:393,height:852},scale:3,sourceKind:'production app-only web template; synthetic loopback fixture; browser-content viewport, without Safari chrome',metrics});
 }
}
writeFileSync(`${dir}/manifest.json`,JSON.stringify(screens,null,2));console.log(JSON.stringify({captured:screens.length,baseScreens:6,directory:dir}));ws.close();
