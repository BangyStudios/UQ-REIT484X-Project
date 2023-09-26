"use strict";(self.webpackChunkmatx_react=self.webpackChunkmatx_react||[]).push([[607],{607:function(e,a,t){t.r(a),t.d(a,{default:function(){return S}});var l=t(4942),r=t(1582),i=t(6934),s=t(4554),n=t(5574),u=t(9439),d=t(2582),c=t(6682),o=t(890),x=t(3963),m=t(2791),b=t(184);function j(){var e=m.useState(30),a=(0,u.Z)(e,2),t=a[0],l=a[1];return(0,b.jsxs)(s.Z,{width:200,children:[(0,b.jsx)(o.Z,{id:"continuous-slider",gutterBottom:!0,children:"Volume"}),(0,b.jsxs)(r.Z,{spacing:2,direction:"row",sx:{mb:1},alignItems:"center",children:[(0,b.jsx)(d.Z,{}),(0,b.jsx)(x.ZP,{"aria-label":"Volume",value:t,onChange:function(e,a){l(a)}}),(0,b.jsx)(c.Z,{})]}),(0,b.jsx)(x.ZP,{disabled:!0,defaultValue:30,"aria-label":"Disabled slider"})]})}var h=(0,i.ZP)("div")((function(e){return{width:300,"& .margin":{height:e.theme.spacing(3)}}})),g=[{value:0,label:"0\xb0C"},{value:20,label:"20\xb0C"},{value:37,label:"37\xb0C"},{value:100,label:"100\xb0C"}];function v(e){return"".concat(e,"\xb0C")}function Z(e){return g.findIndex((function(a){return a.value===e}))+1}function p(){return(0,b.jsxs)(h,{children:[(0,b.jsx)(o.Z,{id:"discrete-slider",gutterBottom:!0,children:"Temperature"}),(0,b.jsx)(x.ZP,{marks:!0,step:10,defaultValue:20,valueLabelDisplay:"auto",getAriaValueText:v,"aria-labelledby":"discrete-slider"}),(0,b.jsx)(s.Z,{className:"margin"}),(0,b.jsx)(o.Z,{id:"discrete-slider-custom",gutterBottom:!0,children:"Custom marks"}),(0,b.jsx)(x.ZP,{step:10,marks:g,defaultValue:20,valueLabelDisplay:"auto",getAriaValueText:v,"aria-labelledby":"discrete-slider-custom"}),(0,b.jsx)("div",{className:"margin"}),(0,b.jsx)(o.Z,{id:"discrete-slider-restrict",gutterBottom:!0,children:"Restricted values"}),(0,b.jsx)(x.ZP,{step:null,marks:g,defaultValue:20,valueLabelDisplay:"auto",getAriaValueText:v,valueLabelFormat:Z,"aria-labelledby":"discrete-slider-restrict"}),(0,b.jsx)("div",{className:"margin"}),(0,b.jsx)(o.Z,{id:"discrete-slider-always",gutterBottom:!0,children:"Always visible"}),(0,b.jsx)(x.ZP,{step:10,marks:g,defaultValue:80,valueLabelDisplay:"on",getAriaValueText:v,"aria-labelledby":"discrete-slider-always"})]})}var f=t(1889),y=t(4110);function V(){var e=m.useState(30),a=(0,u.Z)(e,2),t=a[0],l=a[1];return(0,b.jsxs)(s.Z,{width:250,children:[(0,b.jsx)(o.Z,{id:"input-slider",gutterBottom:!0,children:"Volume"}),(0,b.jsxs)(f.ZP,{container:!0,spacing:2,alignItems:"center",children:[(0,b.jsx)(f.ZP,{item:!0,children:(0,b.jsx)(c.Z,{})}),(0,b.jsx)(f.ZP,{item:!0,xs:!0,children:(0,b.jsx)(x.ZP,{value:"number"===typeof t?t:0,onChange:function(e,a){l(a)},"aria-labelledby":"input-slider"})}),(0,b.jsx)(f.ZP,{item:!0,children:(0,b.jsx)(y.Z,{value:t,margin:"dense",sx:{width:42},onChange:function(e){l(""===e.target.value?"":Number(e.target.value))},onBlur:function(){t<0?l(0):t>100&&l(100)},inputProps:{step:10,min:0,max:100,type:"number","aria-labelledby":"input-slider"}})})]})]})}function C(e){return"".concat(e,"\xb0C")}function P(){var e=m.useState([20,37]),a=(0,u.Z)(e,2),t=a[0],l=a[1];return(0,b.jsxs)(s.Z,{width:300,children:[(0,b.jsx)(o.Z,{id:"range-slider",gutterBottom:!0,children:"Temperature range"}),(0,b.jsx)(x.ZP,{value:t,onChange:function(e,a){l(a)},valueLabelDisplay:"auto","aria-labelledby":"range-slider",getAriaValueText:C})]})}function w(e){return"".concat(e,"\xb0C")}var k=[{value:0,label:"0\xb0C"},{value:20,label:"20\xb0C"},{value:37,label:"37\xb0C"},{value:100,label:"100\xb0C"}];function B(){return(0,b.jsxs)(m.Fragment,{children:[(0,b.jsx)(o.Z,{id:"vertical-slider",gutterBottom:!0,children:"Temperature"}),(0,b.jsxs)(s.Z,{height:300,children:[(0,b.jsx)(x.ZP,{orientation:"vertical",getAriaValueText:w,defaultValue:30,"aria-labelledby":"vertical-slider"}),(0,b.jsx)(x.ZP,{disabled:!0,orientation:"vertical",getAriaValueText:w,defaultValue:30,"aria-labelledby":"vertical-slider"}),(0,b.jsx)(x.ZP,{orientation:"vertical",defaultValue:[20,37],"aria-labelledby":"vertical-slider",getAriaValueText:w,marks:k})]})]})}var T=(0,i.ZP)("div")((function(e){var a,t=e.theme;return a={margin:"30px"},(0,l.Z)(a,t.breakpoints.down("sm"),{margin:"16px"}),(0,l.Z)(a,"& .breadcrumb",(0,l.Z)({marginBottom:"30px"},t.breakpoints.down("sm"),{marginBottom:"16px"})),a})),S=function(){return(0,b.jsxs)(T,{children:[(0,b.jsx)(s.Z,{className:"breadcrumb",children:(0,b.jsx)(n.aG,{routeSegments:[{name:"Material",path:"/material"},{name:"Slider"}]})}),(0,b.jsxs)(r.Z,{spacing:3,children:[(0,b.jsx)(n.sF,{title:"Continuous Slider",children:(0,b.jsx)(j,{})}),(0,b.jsx)(n.sF,{title:"Discrete Slider",children:(0,b.jsx)(p,{})}),(0,b.jsx)(n.sF,{title:"Range Slider",children:(0,b.jsx)(P,{})}),(0,b.jsx)(n.sF,{title:"Slider with Input",children:(0,b.jsx)(V,{})}),(0,b.jsx)(n.sF,{title:"Vertical Slider",children:(0,b.jsx)(B,{})})]})]})}}}]);
//# sourceMappingURL=607.46687ff4.chunk.js.map