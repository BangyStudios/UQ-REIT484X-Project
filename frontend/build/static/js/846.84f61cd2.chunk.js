"use strict";(self.webpackChunkmatx_react=self.webpackChunkmatx_react||[]).push([[846],{8846:function(e,n,t){t.r(n),t.d(n,{default:function(){return he}});var a,o,r,i,s,c,l,u,d=t(4942),p=t(6934),h=t(4554),m=t(5574),g=t(9439),Z=t(9836),x=t(6890),b=t(5855),j=t(3994),f=t(3382),v=t(3400),y=t(9875),P=t(3366),w=t(7462),L=t(2791),R=t(8182),T=t(4419),B=t(627),C=t(1402),I=t(4834),M=t(3786),S=t(8406),k=t(4663),A=t(4223),F=t(184),D=(0,A.Z)((0,F.jsx)("path",{d:"M15.41 16.09l-4.58-4.59 4.58-4.59L14 5.5l-6 6 6 6z"}),"KeyboardArrowLeft"),N=(0,A.Z)((0,F.jsx)("path",{d:"M8.59 16.34l4.58-4.59-4.58-4.59L10 5.75l6 6-6 6z"}),"KeyboardArrowRight"),z=t(3967),G=(0,A.Z)((0,F.jsx)("path",{d:"M5.59 7.41L10.18 12l-4.59 4.59L7 18l6-6-6-6zM16 6h2v12h-2z"}),"LastPage"),H=(0,A.Z)((0,F.jsx)("path",{d:"M18.41 16.59L13.82 12l4.59-4.59L17 6l-6 6 6 6zM6 6h2v12H6z"}),"FirstPage"),O=["backIconButtonProps","count","getItemAriaLabel","nextIconButtonProps","onPageChange","page","rowsPerPage","showFirstButton","showLastButton"],K=L.forwardRef((function(e,n){var t=e.backIconButtonProps,d=e.count,p=e.getItemAriaLabel,h=e.nextIconButtonProps,m=e.onPageChange,g=e.page,Z=e.rowsPerPage,x=e.showFirstButton,b=e.showLastButton,j=(0,P.Z)(e,O),f=(0,z.Z)();return(0,F.jsxs)("div",(0,w.Z)({ref:n},j,{children:[x&&(0,F.jsx)(v.Z,{onClick:function(e){m(e,0)},disabled:0===g,"aria-label":p("first",g),title:p("first",g),children:"rtl"===f.direction?a||(a=(0,F.jsx)(G,{})):o||(o=(0,F.jsx)(H,{}))}),(0,F.jsx)(v.Z,(0,w.Z)({onClick:function(e){m(e,g-1)},disabled:0===g,color:"inherit","aria-label":p("previous",g),title:p("previous",g)},t,{children:"rtl"===f.direction?r||(r=(0,F.jsx)(N,{})):i||(i=(0,F.jsx)(D,{}))})),(0,F.jsx)(v.Z,(0,w.Z)({onClick:function(e){m(e,g+1)},disabled:-1!==d&&g>=Math.ceil(d/Z)-1,color:"inherit","aria-label":p("next",g),title:p("next",g)},h,{children:"rtl"===f.direction?s||(s=(0,F.jsx)(D,{})):c||(c=(0,F.jsx)(N,{}))})),b&&(0,F.jsx)(v.Z,{onClick:function(e){m(e,Math.max(0,Math.ceil(d/Z)-1))},disabled:g>=Math.ceil(d/Z)-1,"aria-label":p("last",g),title:p("last",g),children:"rtl"===f.direction?l||(l=(0,F.jsx)(H,{})):u||(u=(0,F.jsx)(G,{}))})]}))})),$=t(7384),_=t(5878),E=t(1217);function q(e){return(0,E.Z)("MuiTablePagination",e)}var J,Q=(0,_.Z)("MuiTablePagination",["root","toolbar","spacer","selectLabel","selectRoot","select","selectIcon","input","menuItem","displayedRows","actions"]),U=["ActionsComponent","backIconButtonProps","className","colSpan","component","count","getItemAriaLabel","labelDisplayedRows","labelRowsPerPage","nextIconButtonProps","onPageChange","onRowsPerPageChange","page","rowsPerPage","rowsPerPageOptions","SelectProps","showFirstButton","showLastButton"],V=(0,p.ZP)(j.Z,{name:"MuiTablePagination",slot:"Root",overridesResolver:function(e,n){return n.root}})((function(e){var n=e.theme;return{overflow:"auto",color:(n.vars||n).palette.text.primary,fontSize:n.typography.pxToRem(14),"&:last-child":{padding:0}}})),W=(0,p.ZP)(k.Z,{name:"MuiTablePagination",slot:"Toolbar",overridesResolver:function(e,n){return(0,w.Z)((0,d.Z)({},"& .".concat(Q.actions),n.actions),n.toolbar)}})((function(e){var n,t=e.theme;return n={minHeight:52,paddingRight:2},(0,d.Z)(n,"".concat(t.breakpoints.up("xs")," and (orientation: landscape)"),{minHeight:52}),(0,d.Z)(n,t.breakpoints.up("sm"),{minHeight:52,paddingRight:2}),(0,d.Z)(n,"& .".concat(Q.actions),{flexShrink:0,marginLeft:20}),n})),X=(0,p.ZP)("div",{name:"MuiTablePagination",slot:"Spacer",overridesResolver:function(e,n){return n.spacer}})({flex:"1 1 100%"}),Y=(0,p.ZP)("p",{name:"MuiTablePagination",slot:"SelectLabel",overridesResolver:function(e,n){return n.selectLabel}})((function(e){var n=e.theme;return(0,w.Z)({},n.typography.body2,{flexShrink:0})})),ee=(0,p.ZP)(S.Z,{name:"MuiTablePagination",slot:"Select",overridesResolver:function(e,n){var t;return(0,w.Z)((t={},(0,d.Z)(t,"& .".concat(Q.selectIcon),n.selectIcon),(0,d.Z)(t,"& .".concat(Q.select),n.select),t),n.input,n.selectRoot)}})((0,d.Z)({color:"inherit",fontSize:"inherit",flexShrink:0,marginRight:32,marginLeft:8},"& .".concat(Q.select),{paddingLeft:8,paddingRight:24,textAlign:"right",textAlignLast:"right"})),ne=(0,p.ZP)(M.Z,{name:"MuiTablePagination",slot:"MenuItem",overridesResolver:function(e,n){return n.menuItem}})({}),te=(0,p.ZP)("p",{name:"MuiTablePagination",slot:"DisplayedRows",overridesResolver:function(e,n){return n.displayedRows}})((function(e){var n=e.theme;return(0,w.Z)({},n.typography.body2,{flexShrink:0})}));function ae(e){var n=e.from,t=e.to,a=e.count;return"".concat(n,"\u2013").concat(t," of ").concat(-1!==a?a:"more than ".concat(t))}function oe(e){return"Go to ".concat(e," page")}var re=L.forwardRef((function(e,n){var t,a=(0,C.Z)({props:e,name:"MuiTablePagination"}),o=a.ActionsComponent,r=void 0===o?K:o,i=a.backIconButtonProps,s=a.className,c=a.colSpan,l=a.component,u=void 0===l?j.Z:l,d=a.count,p=a.getItemAriaLabel,h=void 0===p?oe:p,m=a.labelDisplayedRows,g=void 0===m?ae:m,Z=a.labelRowsPerPage,x=void 0===Z?"Rows per page:":Z,b=a.nextIconButtonProps,f=a.onPageChange,v=a.onRowsPerPageChange,y=a.page,M=a.rowsPerPage,S=a.rowsPerPageOptions,k=void 0===S?[10,25,50,100]:S,A=a.SelectProps,D=void 0===A?{}:A,N=a.showFirstButton,z=void 0!==N&&N,G=a.showLastButton,H=void 0!==G&&G,O=(0,P.Z)(a,U),_=a,E=function(e){var n=e.classes;return(0,T.Z)({root:["root"],toolbar:["toolbar"],spacer:["spacer"],selectLabel:["selectLabel"],select:["select"],input:["input"],selectIcon:["selectIcon"],menuItem:["menuItem"],displayedRows:["displayedRows"],actions:["actions"]},q,n)}(_),Q=D.native?"option":ne;u!==j.Z&&"td"!==u||(t=c||1e3);var re=(0,$.Z)(D.id),ie=(0,$.Z)(D.labelId);return(0,F.jsx)(V,(0,w.Z)({colSpan:t,ref:n,as:u,ownerState:_,className:(0,R.Z)(E.root,s)},O,{children:(0,F.jsxs)(W,{className:E.toolbar,children:[(0,F.jsx)(X,{className:E.spacer}),k.length>1&&(0,F.jsx)(Y,{className:E.selectLabel,id:ie,children:x}),k.length>1&&(0,F.jsx)(ee,(0,w.Z)({variant:"standard"},!D.variant&&{input:J||(J=(0,F.jsx)(I.ZP,{}))},{value:M,onChange:v,id:re,labelId:ie},D,{classes:(0,w.Z)({},D.classes,{root:(0,R.Z)(E.input,E.selectRoot,(D.classes||{}).root),select:(0,R.Z)(E.select,(D.classes||{}).select),icon:(0,R.Z)(E.selectIcon,(D.classes||{}).icon)}),children:k.map((function(e){return(0,L.createElement)(Q,(0,w.Z)({},!(0,B.Z)(Q)&&{ownerState:_},{className:E.menuItem,key:e.label?e.label:e,value:e.value?e.value:e}),e.label?e.label:e)}))})),(0,F.jsx)(te,{className:E.displayedRows,children:g({from:0===d?0:y*M+1,to:-1===d?(y+1)*M:-1===M?d:Math.min(d,(y+1)*M),count:-1===d?-1:d,page:y})}),(0,F.jsx)(r,{className:E.actions,backIconButtonProps:i,count:d,nextIconButtonProps:b,onPageChange:f,page:y,rowsPerPage:M,showFirstButton:z,showLastButton:H,getItemAriaLabel:h})]})}))})),ie=(0,p.ZP)(Z.Z)((function(){return{whiteSpace:"pre","& thead":{"& tr":{"& th":{paddingLeft:0,paddingRight:0}}},"& tbody":{"& tr":{"& td":{paddingLeft:0,textTransform:"capitalize"}}}}})),se=[{name:"john doe",date:"18 january, 2019",amount:1e3,status:"close",company:"ABC Fintech LTD."},{name:"kessy bryan",date:"10 january, 2019",amount:9e3,status:"open",company:"My Fintech LTD."},{name:"kessy bryan",date:"10 january, 2019",amount:9e3,status:"open",company:"My Fintech LTD."},{name:"james cassegne",date:"8 january, 2019",amount:5e3,status:"close",company:"Collboy Tech LTD."},{name:"lucy brown",date:"1 january, 2019",amount:89e3,status:"open",company:"ABC Fintech LTD."},{name:"lucy brown",date:"1 january, 2019",amount:89e3,status:"open",company:"ABC Fintech LTD."},{name:"lucy brown",date:"1 january, 2019",amount:89e3,status:"open",company:"ABC Fintech LTD."},{name:"lucy brown",date:"1 january, 2019",amount:89e3,status:"open",company:"ABC Fintech LTD."},{name:"lucy brown",date:"1 january, 2019",amount:89e3,status:"open",company:"ABC Fintech LTD."}],ce=function(){var e=(0,L.useState)(0),n=(0,g.Z)(e,2),t=n[0],a=n[1],o=(0,L.useState)(5),r=(0,g.Z)(o,2),i=r[0],s=r[1];return(0,F.jsxs)(h.Z,{width:"100%",overflow:"auto",children:[(0,F.jsxs)(ie,{children:[(0,F.jsx)(x.Z,{children:(0,F.jsxs)(b.Z,{children:[(0,F.jsx)(j.Z,{align:"left",children:"Name"}),(0,F.jsx)(j.Z,{align:"center",children:"Company"}),(0,F.jsx)(j.Z,{align:"center",children:"Start Date"}),(0,F.jsx)(j.Z,{align:"center",children:"Status"}),(0,F.jsx)(j.Z,{align:"center",children:"Amount"}),(0,F.jsx)(j.Z,{align:"right",children:"Action"})]})}),(0,F.jsx)(f.Z,{children:se.slice(t*i,t*i+i).map((function(e,n){return(0,F.jsxs)(b.Z,{children:[(0,F.jsx)(j.Z,{align:"left",children:e.name}),(0,F.jsx)(j.Z,{align:"center",children:e.company}),(0,F.jsx)(j.Z,{align:"center",children:e.date}),(0,F.jsx)(j.Z,{align:"center",children:e.status}),(0,F.jsxs)(j.Z,{align:"center",children:["$",e.amount]}),(0,F.jsx)(j.Z,{align:"right",children:(0,F.jsx)(v.Z,{children:(0,F.jsx)(y.Z,{color:"error",children:"close"})})})]},n)}))})]}),(0,F.jsx)(re,{sx:{px:2},page:t,component:"div",rowsPerPage:i,count:se.length,onPageChange:function(e,n){a(n)},rowsPerPageOptions:[5,10,25],onRowsPerPageChange:function(e){s(+e.target.value),a(0)},nextIconButtonProps:{"aria-label":"Next Page"},backIconButtonProps:{"aria-label":"Previous Page"}})]})},le=(0,p.ZP)(Z.Z)((function(e){e.theme;return{whiteSpace:"pre","& thead":{"& tr":{"& th":{paddingLeft:0,paddingRight:0}}},"& tbody":{"& tr":{"& td":{paddingLeft:0,textTransform:"capitalize"}}}}})),ue=[{name:"john doe",date:"18 january, 2019",amount:1e3,status:"close",company:"ABC Fintech LTD."},{name:"kessy bryan",date:"10 january, 2019",amount:9e3,status:"open",company:"My Fintech LTD."},{name:"james cassegne",date:"8 january, 2019",amount:5e3,status:"close",company:"Collboy Tech LTD."},{name:"lucy brown",date:"1 january, 2019",amount:89e3,status:"open",company:"ABC Fintech LTD."},{name:"lucy brown",date:"1 january, 2019",amount:89e3,status:"open",company:"ABC Fintech LTD."},{name:"lucy brown",date:"1 january, 2019",amount:89e3,status:"open",company:"ABC Fintech LTD."}],de=function(){return(0,F.jsx)(h.Z,{width:"100%",overflow:"auto",children:(0,F.jsxs)(le,{children:[(0,F.jsx)(x.Z,{children:(0,F.jsxs)(b.Z,{children:[(0,F.jsx)(j.Z,{align:"left",children:"Name"}),(0,F.jsx)(j.Z,{align:"center",children:"Company"}),(0,F.jsx)(j.Z,{align:"center",children:"Start Date"}),(0,F.jsx)(j.Z,{align:"center",children:"Status"}),(0,F.jsx)(j.Z,{align:"center",children:"Amount"}),(0,F.jsx)(j.Z,{align:"right",children:"Action"})]})}),(0,F.jsx)(f.Z,{children:ue.map((function(e,n){return(0,F.jsxs)(b.Z,{children:[(0,F.jsx)(j.Z,{align:"left",children:e.name}),(0,F.jsx)(j.Z,{align:"center",children:e.company}),(0,F.jsx)(j.Z,{align:"center",children:e.date}),(0,F.jsx)(j.Z,{align:"center",children:e.status}),(0,F.jsxs)(j.Z,{align:"center",children:["$",e.amount]}),(0,F.jsx)(j.Z,{align:"right",children:(0,F.jsx)(v.Z,{children:(0,F.jsx)(y.Z,{color:"error",children:"close"})})})]},n)}))})]})})},pe=(0,p.ZP)("div")((function(e){var n,t=e.theme;return n={margin:"30px"},(0,d.Z)(n,t.breakpoints.down("sm"),{margin:"16px"}),(0,d.Z)(n,"& .breadcrumb",(0,d.Z)({marginBottom:"30px"},t.breakpoints.down("sm"),{marginBottom:"16px"})),n})),he=function(){return(0,F.jsxs)(pe,{children:[(0,F.jsx)(h.Z,{className:"breadcrumb",children:(0,F.jsx)(m.aG,{routeSegments:[{name:"Material",path:"/material"},{name:"Table"}]})}),(0,F.jsx)(m.sF,{title:"Simple Table",children:(0,F.jsx)(de,{})}),(0,F.jsx)(m.sF,{title:"Pagination Table",children:(0,F.jsx)(ce,{})})]})}},4663:function(e,n,t){t.d(n,{Z:function(){return x}});var a=t(4942),o=t(3366),r=t(7462),i=t(2791),s=t(8182),c=t(4419),l=t(1402),u=t(6934),d=t(5878),p=t(1217);function h(e){return(0,p.Z)("MuiToolbar",e)}(0,d.Z)("MuiToolbar",["root","gutters","regular","dense"]);var m=t(184),g=["className","component","disableGutters","variant"],Z=(0,u.ZP)("div",{name:"MuiToolbar",slot:"Root",overridesResolver:function(e,n){var t=e.ownerState;return[n.root,!t.disableGutters&&n.gutters,n[t.variant]]}})((function(e){var n=e.theme,t=e.ownerState;return(0,r.Z)({position:"relative",display:"flex",alignItems:"center"},!t.disableGutters&&(0,a.Z)({paddingLeft:n.spacing(2),paddingRight:n.spacing(2)},n.breakpoints.up("sm"),{paddingLeft:n.spacing(3),paddingRight:n.spacing(3)}),"dense"===t.variant&&{minHeight:48})}),(function(e){var n=e.theme;return"regular"===e.ownerState.variant&&n.mixins.toolbar})),x=i.forwardRef((function(e,n){var t=(0,l.Z)({props:e,name:"MuiToolbar"}),a=t.className,i=t.component,u=void 0===i?"div":i,d=t.disableGutters,p=void 0!==d&&d,x=t.variant,b=void 0===x?"regular":x,j=(0,o.Z)(t,g),f=(0,r.Z)({},t,{component:u,disableGutters:p,variant:b}),v=function(e){var n=e.classes,t={root:["root",!e.disableGutters&&"gutters",e.variant]};return(0,c.Z)(t,h,n)}(f);return(0,m.jsx)(Z,(0,r.Z)({as:u,className:(0,s.Z)(v.root,a),ref:n,ownerState:f},j))}))},7384:function(e,n,t){var a=t(6248);n.Z=a.Z}}]);
//# sourceMappingURL=846.84f61cd2.chunk.js.map