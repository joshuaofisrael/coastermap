(function(){
var $=function(s,r){return (r||document).querySelector(s)},$$=function(s,r){return Array.prototype.slice.call((r||document).querySelectorAll(s))};
function esc(s){return String(s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
/* sign-up */
$$('.signup-form').forEach(function(f){f.addEventListener('submit',function(e){if(!window.fetch)return;e.preventDefault();var st=$('.form-status',f),b=$('button',f);b.disabled=true;
var d={email:f.email.value,consent:f.consent.checked?'yes':'',company:f.company.value};
fetch(f.action,{method:'POST',headers:{'Content-Type':'application/json','Accept':'application/json'},body:JSON.stringify(d)}).then(function(r){return r.json()}).then(function(j){st.hidden=false;st.className='form-status '+(j.ok?'ok':'err');st.textContent=j.message||(j.ok?'Thanks!':'Sorry, something went wrong.');if(j.ok)f.reset();b.disabled=false})
.catch(function(){st.hidden=false;st.className='form-status err';st.textContent='Sorry, the sign-up could not be sent. Please try again later.';b.disabled=false})})});
if(/[?&]error=1/.test(location.search)&&$('#nl-msg'))$('#nl-msg').textContent='Sorry, that sign-up did not go through. Please go back and try again.';
/* contact */
var cf=$('#contact-form'),cs=$('#contact-status');if(cf&&cs){function show(t,ok){cs.textContent=t;cs.hidden=false;cs.className='form-status '+(ok?'ok':'err')}
if(/[?&]sent=1/.test(location.search)){cf.hidden=true;show('Thank you. Your message has been sent and we will reply to the email address you gave.',true)}
cf.addEventListener('submit',function(e){if(!window.fetch||!window.FormData)return;e.preventDefault();var b=$('button',cf);b.disabled=true;var d=new FormData(cf);d.delete('_next');
fetch(cf.action.replace('formsubmit.co/','formsubmit.co/ajax/'),{method:'POST',body:d,headers:{'Accept':'application/json'}}).then(function(r){return r.json()}).then(function(j){if(j&&(j.success===true||j.success==='true')){cf.reset();cf.hidden=true;show('Thank you. Your message has been sent and we will reply to the email address you gave.',true)}else{throw 0}})
.catch(function(){b.disabled=false;show('Sorry, the message could not be sent. Please try again in a moment.',false)})})}
/* sortable tables */
$$('table.sortable').forEach(function(t){$$('thead th',t).forEach(function(th,i){th.tabIndex=0;th.setAttribute('aria-sort','none');function go(){var rows=$$('tbody tr',t),asc=th.getAttribute('aria-sort')!=='ascending';
rows.sort(function(a,b){var x=a.children[i],y=b.children[i],vx=x.getAttribute('data-v'),vy=y.getAttribute('data-v');if(vx!==null&&vy!==null){return (parseFloat(vx)-parseFloat(vy))*(asc?1:-1)}return x.textContent.localeCompare(y.textContent)*(asc?1:-1)});
$$('thead th',t).forEach(function(h){h.setAttribute('aria-sort','none')});th.setAttribute('aria-sort',asc?'ascending':'descending');rows.forEach(function(r){t.tBodies[0].appendChild(r)})}
th.addEventListener('click',go);th.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();go()}})})});
/* maps */
function initMaps(){if(!window.L)return;$$('.map').forEach(function(el){var dEl=document.getElementById(el.id+'-data');if(!dEl)return;var pts=JSON.parse(dEl.textContent);if(!pts.length){el.hidden=true;return}
var m=L.map(el,{scrollWheelZoom:false});L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png',{maxZoom:19,attribution:'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'}).addTo(m);
var col={Kiddie:'#1b7a3a',Family:'#1b7a3a',Thrill:'#c06a00',Extreme:'#b3001b'},layer=L.featureGroup().addTo(m),all=[];
pts.forEach(function(p){var mk=L.circleMarker([p.lat,p.lon],{radius:8,color:'#14213d',weight:2,fillColor:col[p.s]||'#14213d',fillOpacity:.9});mk.bindPopup('<strong><a href="'+p.u+'">'+esc(p.n)+'</a></strong><br>'+esc(p.p)+'<br>'+(p.h?('Min height '+p.h):'Height rule: check park')+(p.s?'<br>'+esc(p.s):''));mk.bindTooltip(p.n);mk._park=p.p;mk.addTo(layer);all.push(mk)});
if(pts.length===1)m.setView([pts[0].lat,pts[0].lon],17);else m.fitBounds(layer.getBounds(),{padding:[30,30]});
var f=document.querySelector('select[data-map="'+el.id+'"]');if(f)f.addEventListener('change',function(){layer.clearLayers();all.forEach(function(mk){if(!f.value||mk._park===f.value)mk.addTo(layer)});if(layer.getLayers().length)m.fitBounds(layer.getBounds(),{padding:[30,30],maxZoom:17})})})}
if(document.readyState==='complete')initMaps();else window.addEventListener('load',initMaps);
var dataEl=$('#coaster-data'),D=dataEl?JSON.parse(dataEl.textContent):[];
function U(c){return c.mu==='cm'?' cm':' in'}
function li(c,extra){return '<li><a href="'+c.u+'">'+esc(c.n)+'</a> <span class="muted">('+esc(c.p)+(extra?', '+extra:'')+')</span></li>'}
/* height checker */
var hc=$('#hc');if(hc){hc.addEventListener('submit',function(){var v=parseFloat($('#hc-h').value),u=$('#hc-u').value,pk=$('#hc-p').value,out=$('#hc-out');if(!(v>0)){out.innerHTML='<p>Please enter a height.</p>';return}
var inch=u==='cm'?v/2.54:v,cmv=u==='cm'?v:v*2.54,cs=D.filter(function(c){return !pk||c.ps===pk}),ok=[],comp=[],no=[],over=[],unk=[];
cs.forEach(function(c){if(c.min==null){unk.push(c);return}var x=c.mu==='cm'?cmv:inch;if(c.mx&&x>c.mx+1e-9){over.push(c);return}if(x>=c.min-1e-9)ok.push(c);else if(c.am&&x>=c.am-1e-9)comp.push(c);else no.push(c)});
var r='<div class="res"><p><strong>At '+(Math.round(inch*10)/10)+' in ('+(Math.round(cmv*10)/10)+' cm):</strong></p>';
r+='<h3>Can ride ('+ok.length+')</h3><ul>'+ok.map(function(c){return li(c,'min '+c.min+U(c))}).join('')+'</ul>';
if(comp.length)r+='<h3>Can ride with a companion ('+comp.length+')</h3><ul>'+comp.map(function(c){return li(c,c.am+' to '+c.ax+U(c)+' with a companion')}).join('')+'</ul>';
r+='<h3>Not tall enough yet ('+no.length+')</h3><ul>'+no.sort(function(a,b){return (a.mu==='cm'?a.min/2.54:a.min)-(b.mu==='cm'?b.min/2.54:b.min)}).map(function(c){return li(c,'needs '+c.min+U(c)+', '+(Math.ceil((c.min-(c.mu==='cm'?cmv:inch))*10)/10)+U(c)+' to go')}).join('')+'</ul>';
if(over.length)r+='<h3>Over the maximum height ('+over.length+')</h3><ul>'+over.map(function(c){return li(c,'max '+c.mx+U(c))}).join('')+'</ul>';
if(unk.length)r+='<h3>Requirement not verified, ask the park ('+unk.length+')</h3><ul>'+unk.map(function(c){return li(c)}).join('')+'</ul>';
out.innerHTML=r+'<p class="note">Always confirm at the ride entrance. Parks can change rules at any time.</p></div>'})}
/* quiz */
var qz=$('#qz');if(qz){qz.addEventListener('submit',function(){var pk=$('#qz-p').value,h=parseFloat($('#qz-h').value),t=$('input[name="qz-t"]:checked').value,inv=$('input[name="qz-i"]:checked').value,out=$('#qz-out');if(!(h>0)){out.innerHTML='<p>Please enter your height.</p>';return}
var want={gentle:['Kiddie','Family'],moderate:['Family','Thrill'],max:['Extreme']}[t];
var cs=D.filter(function(c){return (!pk||c.ps===pk)&&c.min!=null&&(c.mu==='cm'?h*2.54:h)>=c.min-1e-9&&!(c.mx&&(c.mu==='cm'?h*2.54:h)>c.mx+1e-9)&&want.indexOf(c.s)>=0&&(inv==='yes'||c.i===0)});
if(inv==='yes'&&t!=='gentle'){var withInv=cs.filter(function(c){return c.i>0});if(withInv.length)cs=withInv.concat(cs.filter(function(c){return !(c.i>0)}))}
cs.sort(function(a,b){return t==='gentle'?((a.h||0)-(b.h||0)):((b.h||0)-(a.h||0))});
if(!cs.length){out.innerHTML='<div class="res"><p>No exact match. Try another park or a different thrill level.</p></div>';return}
var top=cs[0];out.innerHTML='<div class="res"><h3>Your coaster: <a href="'+top.u+'">'+esc(top.n)+'</a></h3><p>'+esc(top.p)+(top.h?' · '+top.h+' ft tall':'')+(top.v?' · '+top.v+' mph':'')+' · '+(top.i?top.i+' inversions':'no inversions')+' · min height '+top.min+U(top)+'</p>'+(cs.length>1?'<p>Also try:</p><ul>'+cs.slice(1,6).map(function(c){return li(c,(c.h?c.h+' ft':'')+(c.v?', '+c.v+' mph':''))}).join('')+'</ul>':'')+'<p class="note">Matches use official minimum heights and RCDB intensity classes. Check the park for health and safety rules.</p></div>'})}
/* trivia */
var tg=$('#tg');if(tg){var pool=D.filter(function(c){return c.h}),s=0,best=0;try{best=+localStorage.getItem('cmTallerBest')||0}catch(e){}$('#tg-b').textContent=best;
function round(){var a,b;do{a=pool[Math.floor(Math.random()*pool.length)];b=pool[Math.floor(Math.random()*pool.length)]}while(a===b||a.h===b.h);$('#tg-q').textContent='Which coaster is taller?';var w=$('#tg-btns');w.innerHTML='';
[a,b].forEach(function(c){var bt=document.createElement('button');bt.className='btn alt';bt.type='button';bt.textContent=c.n+' ('+c.p+')';bt.addEventListener('click',function(){var other=c===a?b:a,right=c.h>other.h;s=right?s+1:0;if(s>best){best=s;try{localStorage.setItem('cmTallerBest',best)}catch(e){}}
$('#tg-s').textContent=s;$('#tg-b').textContent=best;$('#tg-msg').innerHTML=(right?'Correct! ':'Not quite. ')+esc(c.n)+' is '+c.h+' ft; '+esc(other.n)+' is '+other.h+' ft. <button type="button" class="btn" id="tg-next">Next pair</button>';$('#tg-next').addEventListener('click',function(){$('#tg-msg').textContent='';round()});$$('#tg-btns button').forEach(function(x){x.disabled=true})});w.appendChild(bt)})}
round()}
})();
