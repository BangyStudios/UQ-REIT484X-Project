(self.webpackChunkmatx_react=self.webpackChunkmatx_react||[]).push([[208],{4208:function(e,t,n){"use strict";n.r(t),n.d(t,{default:function(){return G}});var r=n(4942),o=n(1582),i=n(6934),a=n(4554),c=n(5574),s=n(9439),u=n(6474),l=n(8698),d=n(1686),p=n(6151),m=n(3366),f=n(7462),v=n(2791),Z=n(8182),h=n(4419),x=n(1402),g=n(6014),b=n(6199),y=n(184),j=["className"],k=(0,i.ZP)("div",{name:"MuiListItemIcon",slot:"Root",overridesResolver:function(e,t){var n=e.ownerState;return[t.root,"flex-start"===n.alignItems&&t.alignItemsFlexStart]}})((function(e){var t=e.theme,n=e.ownerState;return(0,f.Z)({minWidth:56,color:(t.vars||t).palette.action.active,flexShrink:0,display:"inline-flex"},"flex-start"===n.alignItems&&{marginTop:8})})),C=v.forwardRef((function(e,t){var n=(0,x.Z)({props:e,name:"MuiListItemIcon"}),r=n.className,o=(0,m.Z)(n,j),i=v.useContext(b.Z),a=(0,f.Z)({},n,{alignItems:i.alignItems}),c=function(e){var t=e.alignItems,n=e.classes,r={root:["root","flex-start"===t&&"alignItemsFlexStart"]};return(0,h.Z)(r,g.f,n)}(a);return(0,y.jsx)(k,(0,f.Z)({className:(0,Z.Z)(c.root,r),ownerState:a,ref:t},o))})),M=n(9900),I=n(911),S=n(3786),w=(0,i.ZP)(S.Z)((function(e){var t=e.theme;return{"&:focus":{backgroundColor:t.palette.primary.main,"& .MuiListItemIcon-root, & .MuiListItemText-primary":{color:t.palette.common.white}}}}));var P=function(){var e=v.useState(null),t=(0,s.Z)(e,2),n=t[0],r=t[1];return(0,y.jsxs)("div",{children:[(0,y.jsx)(p.Z,{color:"primary",variant:"contained","aria-haspopup":"true",onClick:function(e){r(e.currentTarget)},"aria-owns":n?"simple-menu":void 0,children:"Open Menu"}),(0,y.jsxs)(I.Z,{elevation:0,id:"simple-menu",anchorEl:n,onClose:function(){r(null)},open:Boolean(n),getContentAnchorEl:null,anchorOrigin:{vertical:"bottom",horizontal:"center"},transformOrigin:{vertical:"top",horizontal:"center"},sx:{border:"1px solid #d3d4d5"},children:[(0,y.jsxs)(w,{children:[(0,y.jsx)(C,{children:(0,y.jsx)(d.Z,{})}),(0,y.jsx)(M.Z,{primary:"Sent mail"})]}),(0,y.jsxs)(w,{children:[(0,y.jsx)(C,{children:(0,y.jsx)(u.Z,{})}),(0,y.jsx)(M.Z,{primary:"Drafts"})]}),(0,y.jsxs)(w,{children:[(0,y.jsx)(C,{children:(0,y.jsx)(l.Z,{})}),(0,y.jsx)(M.Z,{primary:"Inbox"})]})]})]})},O=n(3400),T=n(9875),F=["None","Atria","Callisto","Dione","Ganymede","Hangouts Call","Luna","Oberon","Phobos","Pyxis","Sedna","Titania","Triton","Umbriel"],L=48;var N=function(){var e=v.useState(null),t=(0,s.Z)(e,2),n=t[0],r=t[1],o=Boolean(n);function i(){r(null)}return(0,y.jsxs)(a.Z,{children:[(0,y.jsx)(O.Z,{"aria-label":"More","aria-owns":o?"long-menu":void 0,"aria-haspopup":"true",onClick:function(e){r(e.currentTarget)},children:(0,y.jsx)(T.Z,{children:"more_vert"})}),(0,y.jsx)(I.Z,{open:o,id:"long-menu",anchorEl:n,onClose:i,PaperProps:{style:{maxHeight:4.5*L,width:200}},children:F.map((function(e){return(0,y.jsx)(S.Z,{selected:"Pyxis"===e,onClick:i,children:e},e)}))})]})},R=n(493),B=n(4852),z=(0,i.ZP)("div")((function(e){return{width:"100%",maxWidth:360,backgroundColor:e.theme.palette.background.paper}})),H=["Show some love to Material-UI","Show all notification content","Hide sensitive notification content","Hide all notification content"];function _(){var e=v.useState(null),t=(0,s.Z)(e,2),n=t[0],r=t[1],o=v.useState(1),i=(0,s.Z)(o,2),a=i[0],c=i[1];return(0,y.jsxs)(z,{children:[(0,y.jsx)(R.Z,{component:"nav","aria-label":"Device settings",children:(0,y.jsx)(B.ZP,{button:!0,"aria-haspopup":"true","aria-controls":"lock-menu","aria-label":"When device is locked",onClick:function(e){r(e.currentTarget)},children:(0,y.jsx)(M.Z,{primary:"When device is locked",secondary:H[a]})})}),(0,y.jsx)(I.Z,{id:"lock-menu",anchorEl:n,keepMounted:!0,open:Boolean(n),onClose:function(){r(null)},children:H.map((function(e,t){return(0,y.jsx)(S.Z,{disabled:0===t,selected:t===a,onClick:function(e){return function(e,t){c(t),r(null)}(0,t)},children:e},e)}))})]})}var E=function(){var e=v.useState(null),t=(0,s.Z)(e,2),n=t[0],r=t[1];function o(){r(null)}return(0,y.jsxs)(a.Z,{children:[(0,y.jsx)(p.Z,{variant:"outlined","aria-haspopup":"true",onClick:function(e){r(e.currentTarget)},"aria-owns":n?"simple-menu":void 0,children:"Open Menu"}),(0,y.jsxs)(I.Z,{id:"simple-menu",anchorEl:n,open:Boolean(n),onClose:o,children:[(0,y.jsx)(S.Z,{onClick:o,children:"Profile"}),(0,y.jsx)(S.Z,{onClick:o,children:"My account"}),(0,y.jsx)(S.Z,{onClick:o,children:"Logout"})]})]})},V=(0,i.ZP)("div")((function(e){var t,n=e.theme;return t={margin:"30px"},(0,r.Z)(t,n.breakpoints.down("sm"),{margin:16}),(0,r.Z)(t,"& .breadcrumb",(0,r.Z)({marginBottom:"30px"},n.breakpoints.down("sm"),{marginBottom:16})),t})),G=function(){return(0,y.jsxs)(V,{children:[(0,y.jsx)(a.Z,{className:"breadcrumb",children:(0,y.jsx)(c.aG,{routeSegments:[{name:"Material",path:"/material"},{name:"Menu"}]})}),(0,y.jsxs)(o.Z,{spacing:3,children:[(0,y.jsx)(c.sF,{title:"simple menu",children:(0,y.jsx)(E,{})}),(0,y.jsx)(c.sF,{title:"selected menu",children:(0,y.jsx)(_,{})}),(0,y.jsx)(c.sF,{title:"customized menu",children:(0,y.jsx)(P,{})}),(0,y.jsx)(c.sF,{title:"max height menu",children:(0,y.jsx)(N,{})})]})]})}},6474:function(e,t,n){"use strict";var r=n(4836);t.Z=void 0;var o=r(n(5649)),i=n(184),a=(0,o.default)((0,i.jsx)("path",{d:"M21.99 8c0-.72-.37-1.35-.94-1.7L12 1 2.95 6.3C2.38 6.65 2 7.28 2 8v10c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2l-.01-10zM12 13 3.74 7.84 12 3l8.26 4.84L12 13z"}),"Drafts");t.Z=a},8698:function(e,t,n){"use strict";var r=n(4836);t.Z=void 0;var o=r(n(5649)),i=n(184),a=(0,o.default)((0,i.jsx)("path",{d:"M19 3H4.99c-1.11 0-1.98.9-1.98 2L3 19c0 1.1.88 2 1.99 2H19c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 12h-4c0 1.66-1.35 3-3 3s-3-1.34-3-3H4.99V5H19v10zm-3-5h-2V7h-4v3H8l4 4 4-4z"}),"MoveToInbox");t.Z=a},1686:function(e,t,n){"use strict";var r=n(4836);t.Z=void 0;var o=r(n(5649)),i=n(184),a=(0,o.default)((0,i.jsx)("path",{d:"M2.01 21 23 12 2.01 3 2 10l15 2-15 2z"}),"Send");t.Z=a},5649:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),Object.defineProperty(t,"default",{enumerable:!0,get:function(){return r.createSvgIcon}});var r=n(9626)},6014:function(e,t,n){"use strict";n.d(t,{f:function(){return i}});var r=n(5878),o=n(1217);function i(e){return(0,o.Z)("MuiListItemIcon",e)}var a=(0,r.Z)("MuiListItemIcon",["root","alignItemsFlexStart"]);t.Z=a},9849:function(e,t,n){"use strict";n.d(t,{L:function(){return i}});var r=n(5878),o=n(1217);function i(e){return(0,o.Z)("MuiListItemText",e)}var a=(0,r.Z)("MuiListItemText",["root","multiline","dense","inset","primary","secondary"]);t.Z=a},3786:function(e,t,n){"use strict";n.d(t,{Z:function(){return I}});var r=n(4942),o=n(3366),i=n(7462),a=n(2791),c=n(8182),s=n(4419),u=n(2065),l=n(6934),d=n(1402),p=n(6199),m=n(3701),f=n(162),v=n(2071),Z=n(133),h=n(6014),x=n(9849),g=n(5878),b=n(1217);function y(e){return(0,b.Z)("MuiMenuItem",e)}var j=(0,g.Z)("MuiMenuItem",["root","focusVisible","dense","disabled","divider","gutters","selected"]),k=n(184),C=["autoFocus","component","dense","divider","disableGutters","focusVisibleClassName","role","tabIndex","className"],M=(0,l.ZP)(m.Z,{shouldForwardProp:function(e){return(0,l.FO)(e)||"classes"===e},name:"MuiMenuItem",slot:"Root",overridesResolver:function(e,t){var n=e.ownerState;return[t.root,n.dense&&t.dense,n.divider&&t.divider,!n.disableGutters&&t.gutters]}})((function(e){var t,n=e.theme,o=e.ownerState;return(0,i.Z)({},n.typography.body1,{display:"flex",justifyContent:"flex-start",alignItems:"center",position:"relative",textDecoration:"none",minHeight:48,paddingTop:6,paddingBottom:6,boxSizing:"border-box",whiteSpace:"nowrap"},!o.disableGutters&&{paddingLeft:16,paddingRight:16},o.divider&&{borderBottom:"1px solid ".concat((n.vars||n).palette.divider),backgroundClip:"padding-box"},(t={"&:hover":{textDecoration:"none",backgroundColor:(n.vars||n).palette.action.hover,"@media (hover: none)":{backgroundColor:"transparent"}}},(0,r.Z)(t,"&.".concat(j.selected),(0,r.Z)({backgroundColor:n.vars?"rgba(".concat(n.vars.palette.primary.mainChannel," / ").concat(n.vars.palette.action.selectedOpacity,")"):(0,u.Fq)(n.palette.primary.main,n.palette.action.selectedOpacity)},"&.".concat(j.focusVisible),{backgroundColor:n.vars?"rgba(".concat(n.vars.palette.primary.mainChannel," / calc(").concat(n.vars.palette.action.selectedOpacity," + ").concat(n.vars.palette.action.focusOpacity,"))"):(0,u.Fq)(n.palette.primary.main,n.palette.action.selectedOpacity+n.palette.action.focusOpacity)})),(0,r.Z)(t,"&.".concat(j.selected,":hover"),{backgroundColor:n.vars?"rgba(".concat(n.vars.palette.primary.mainChannel," / calc(").concat(n.vars.palette.action.selectedOpacity," + ").concat(n.vars.palette.action.hoverOpacity,"))"):(0,u.Fq)(n.palette.primary.main,n.palette.action.selectedOpacity+n.palette.action.hoverOpacity),"@media (hover: none)":{backgroundColor:n.vars?"rgba(".concat(n.vars.palette.primary.mainChannel," / ").concat(n.vars.palette.action.selectedOpacity,")"):(0,u.Fq)(n.palette.primary.main,n.palette.action.selectedOpacity)}}),(0,r.Z)(t,"&.".concat(j.focusVisible),{backgroundColor:(n.vars||n).palette.action.focus}),(0,r.Z)(t,"&.".concat(j.disabled),{opacity:(n.vars||n).palette.action.disabledOpacity}),(0,r.Z)(t,"& + .".concat(Z.Z.root),{marginTop:n.spacing(1),marginBottom:n.spacing(1)}),(0,r.Z)(t,"& + .".concat(Z.Z.inset),{marginLeft:52}),(0,r.Z)(t,"& .".concat(x.Z.root),{marginTop:0,marginBottom:0}),(0,r.Z)(t,"& .".concat(x.Z.inset),{paddingLeft:36}),(0,r.Z)(t,"& .".concat(h.Z.root),{minWidth:36}),t),!o.dense&&(0,r.Z)({},n.breakpoints.up("sm"),{minHeight:"auto"}),o.dense&&(0,i.Z)({minHeight:32,paddingTop:4,paddingBottom:4},n.typography.body2,(0,r.Z)({},"& .".concat(h.Z.root," svg"),{fontSize:"1.25rem"})))})),I=a.forwardRef((function(e,t){var n=(0,d.Z)({props:e,name:"MuiMenuItem"}),r=n.autoFocus,u=void 0!==r&&r,l=n.component,m=void 0===l?"li":l,Z=n.dense,h=void 0!==Z&&Z,x=n.divider,g=void 0!==x&&x,b=n.disableGutters,j=void 0!==b&&b,I=n.focusVisibleClassName,S=n.role,w=void 0===S?"menuitem":S,P=n.tabIndex,O=n.className,T=(0,o.Z)(n,C),F=a.useContext(p.Z),L=a.useMemo((function(){return{dense:h||F.dense||!1,disableGutters:j}}),[F.dense,h,j]),N=a.useRef(null);(0,f.Z)((function(){u&&N.current&&N.current.focus()}),[u]);var R,B=(0,i.Z)({},n,{dense:L.dense,divider:g,disableGutters:j}),z=function(e){var t=e.disabled,n=e.dense,r=e.divider,o=e.disableGutters,a=e.selected,c=e.classes,u={root:["root",n&&"dense",t&&"disabled",!o&&"gutters",r&&"divider",a&&"selected"]},l=(0,s.Z)(u,y,c);return(0,i.Z)({},c,l)}(n),H=(0,v.Z)(N,t);return n.disabled||(R=void 0!==P?P:-1),(0,k.jsx)(p.Z.Provider,{value:L,children:(0,k.jsx)(M,(0,i.Z)({ref:H,role:w,tabIndex:R,component:m,focusVisibleClassName:(0,c.Z)(z.focusVisible,I),className:(0,c.Z)(z.root,O)},T,{ownerState:B,classes:z}))})}))},1582:function(e,t,n){"use strict";n.d(t,{Z:function(){return S}});var r=n(4942),o=n(3366),i=n(7462),a=n(2791),c=n(8182),s=n(2466),u=n(4419),l=n(1217),d=(0,n(4046).ZP)(),p=n(6083),m=n(8519),f=n(5080),v=n(1184),Z=n(5682),h=n(184),x=["component","direction","spacing","divider","children","className"],g=(0,f.Z)(),b=d("div",{name:"MuiStack",slot:"Root",overridesResolver:function(e,t){return t.root}});function y(e){return(0,p.Z)({props:e,name:"MuiStack",defaultTheme:g})}function j(e,t){var n=a.Children.toArray(e).filter(Boolean);return n.reduce((function(e,r,o){return e.push(r),o<n.length-1&&e.push(a.cloneElement(t,{key:"separator-".concat(o)})),e}),[])}var k=function(e){var t=e.ownerState,n=e.theme,o=(0,i.Z)({display:"flex",flexDirection:"column"},(0,v.k9)({theme:n},(0,v.P$)({values:t.direction,breakpoints:n.breakpoints.values}),(function(e){return{flexDirection:e}})));if(t.spacing){var a=(0,Z.hB)(n),c=Object.keys(n.breakpoints.values).reduce((function(e,n){return("object"===typeof t.spacing&&null!=t.spacing[n]||"object"===typeof t.direction&&null!=t.direction[n])&&(e[n]=!0),e}),{}),u=(0,v.P$)({values:t.direction,base:c}),l=(0,v.P$)({values:t.spacing,base:c});"object"===typeof u&&Object.keys(u).forEach((function(e,t,n){if(!u[e]){var r=t>0?u[n[t-1]]:"column";u[e]=r}}));o=(0,s.Z)(o,(0,v.k9)({theme:n},l,(function(e,n){return{"& > :not(style) + :not(style)":(0,r.Z)({margin:0},"margin".concat((o=n?u[n]:t.direction,{row:"Left","row-reverse":"Right",column:"Top","column-reverse":"Bottom"}[o])),(0,Z.NA)(a,e))};var o})))}return o=(0,v.dt)(n.breakpoints,o)};var C=n(6934),M=n(1402),I=function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{},t=e.createStyledComponent,n=void 0===t?b:t,r=e.useThemeProps,s=void 0===r?y:r,d=e.componentName,p=void 0===d?"MuiStack":d,f=n(k),v=a.forwardRef((function(e,t){var n=s(e),r=(0,m.Z)(n),a=r.component,d=void 0===a?"div":a,v=r.direction,Z=void 0===v?"column":v,g=r.spacing,b=void 0===g?0:g,y=r.divider,k=r.children,C=r.className,M=(0,o.Z)(r,x),I={direction:Z,spacing:b},S=(0,u.Z)({root:["root"]},(function(e){return(0,l.Z)(p,e)}),{});return(0,h.jsx)(f,(0,i.Z)({as:d,ownerState:I,ref:t,className:(0,c.Z)(S.root,C)},M,{children:y?j(k,y):k}))}));return v}({createStyledComponent:(0,C.ZP)("div",{name:"MuiStack",slot:"Root",overridesResolver:function(e,t){return t.root}}),useThemeProps:function(e){return(0,M.Z)({props:e,name:"MuiStack"})}}),S=I},1260:function(e,t,n){"use strict";var r=n(8949);t.Z=r.Z},9626:function(e,t,n){"use strict";n.r(t),n.d(t,{capitalize:function(){return o.Z},createChainedFunction:function(){return i.Z},createSvgIcon:function(){return a.Z},debounce:function(){return c.Z},deprecatedPropType:function(){return s},isMuiElement:function(){return u.Z},ownerDocument:function(){return l.Z},ownerWindow:function(){return d.Z},requirePropFactory:function(){return p},setRef:function(){return m},unstable_ClassNameGenerator:function(){return y},unstable_useEnhancedEffect:function(){return f.Z},unstable_useId:function(){return v.Z},unsupportedProp:function(){return Z},useControlled:function(){return h.Z},useEventCallback:function(){return x.Z},useForkRef:function(){return g.Z},useIsFocusVisible:function(){return b.Z}});var r=n(5902),o=n(4036),i=n(1260),a=n(4223),c=n(3199);var s=function(e,t){return function(){return null}},u=n(9103),l=n(8301),d=n(7602);n(7462);var p=function(e,t){return function(){return null}},m=n(2971).Z,f=n(162),v=n(7384);var Z=function(e,t,n,r,o){return null},h=n(4556),x=n(9683),g=n(2071),b=n(8221),y={configure:function(e){r.Z.configure(e)}}},7384:function(e,t,n){"use strict";var r=n(6248);t.Z=r.Z},4836:function(e){e.exports=function(e){return e&&e.__esModule?e:{default:e}},e.exports.__esModule=!0,e.exports.default=e.exports}}]);
//# sourceMappingURL=208.b0b7710d.chunk.js.map