!function(t){var e={};function r(n){if(e[n])return e[n].exports;var o=e[n]={i:n,l:!1,exports:{}};return t[n].call(o.exports,o,o.exports,r),o.l=!0,o.exports}r.m=t,r.c=e,r.d=function(t,e,n){r.o(t,e)||Object.defineProperty(t,e,{configurable:!1,enumerable:!0,get:n})},r.r=function(t){Object.defineProperty(t,"__esModule",{value:!0})},r.n=function(t){var e=t&&t.__esModule?function(){return t.default}:function(){return t};return r.d(e,"a",e),e},r.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},r.p="",r(r.s=7)}([function(t,e,r){"use strict";Object.defineProperty(e,"__esModule",{value:!0}),(e.memoize=function t(e,r){if("function"!=typeof e||r&&"function"!=typeof r)throw new TypeError("Expected a function");var n=function t(){for(var n=arguments.length,o=Array(n),i=0;i<n;i++)o[i]=arguments[i];var s=r?r.apply(void 0,o):o[0],a=t.cache;if(a.has(s))return a.get(s);var u=e.apply(void 0,o);return t.cache=a.set(s,u)||a,u};return n.cache=new t.Cache,n}).Cache=Map},function(t,e,r){"use strict";Object.defineProperty(e,"__esModule",{value:!0}),e.getExpiresIn=void 0;var n,o,i=["ridibooks.com","dev.ridi.io","dev.ridi.com"],s=(0,r(0).memoize)(function(){for(var t=window.location.host,e=0;e<i.length;e+=1)if(t.includes(i[e]))return i[e];throw new Error("This site not allowed")},function(){return"account-domain"});e.getExpiresIn=(n=regeneratorRuntime.mark(function t(){var e,r;return regeneratorRuntime.wrap(function(t){for(;;)switch(t.prev=t.next){case 0:return t.next=2,fetch("https://account."+s()+"/ridi/token/",{method:"POST",credentials:"include"});case 2:return e=t.sent,t.next=5,e.json();case 5:return r=t.sent,t.abrupt("return",r.expires_in);case 7:case"end":return t.stop()}},t,void 0)}),o=function(){var t=n.apply(this,arguments);return new Promise(function(e,r){return function n(o,i){try{var s=t[o](i),a=s.value}catch(t){return void r(t)}if(!s.done)return Promise.resolve(a).then(function(t){n("next",t)},function(t){n("throw",t)});e(a)}("next")})},function(){return o.apply(this,arguments)})},function(t,e,r){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var n=e.DEFAULT_INTERVAL_MARGIN=300,o=e.MICROSECONDS=1e3;e.calcInterval=function(t){var e=arguments.length>1&&void 0!==arguments[1]?arguments[1]:n;return t<e?0:t*o-e*o}},function(t,e,r){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var n=r(2);Object.keys(n).forEach(function(t){"default"!==t&&"__esModule"!==t&&Object.defineProperty(e,t,{enumerable:!0,get:function(){return n[t]}})});var o=r(1);Object.keys(o).forEach(function(t){"default"!==t&&"__esModule"!==t&&Object.defineProperty(e,t,{enumerable:!0,get:function(){return o[t]}})});var i=r(0);Object.keys(i).forEach(function(t){"default"!==t&&"__esModule"!==t&&Object.defineProperty(e,t,{enumerable:!0,get:function(){return i[t]}})})},function(t,e,r){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var n=r(3),o=function(){function t(){!function(t,e){if(!(t instanceof e))throw new TypeError("Cannot call a class as a function")}(this,t),this.timeoutId=null,this.retryCount=0,this._loop=this._loop.bind(this)}return t.prototype.start=function(){this.isRunning()||(this.timeoutId=setTimeout(this._loop,0))},t.prototype.stop=function(){clearTimeout(this.timeoutId),this.timeoutId=null},t.prototype.isRunning=function(){return null!==this.timeoutId},t.prototype._loop=function(){var t,e=(t=regeneratorRuntime.mark(function t(){var e,r;return regeneratorRuntime.wrap(function(t){for(;;)switch(t.prev=t.next){case 0:return e=null,t.prev=1,t.next=4,(0,n.getExpiresIn)();case 4:e=t.sent,t.next=11;break;case 7:return t.prev=7,t.t0=t.catch(1),this.retryCount<3?(this.retryCount+=1,this.timeoutId=setTimeout(this._loop,5e3)):this.stop(),t.abrupt("return");case 11:r=(0,n.calcInterval)(e),this.retryCount=0,this.timeoutId=setTimeout(this._loop,r);case 14:case"end":return t.stop()}},t,this,[[1,7]])}),function(){var e=t.apply(this,arguments);return new Promise(function(t,r){return function n(o,i){try{var s=e[o](i),a=s.value}catch(t){return void r(t)}if(!s.done)return Promise.resolve(a).then(function(t){n("next",t)},function(t){n("throw",t)});t(a)}("next")})});return function(){return e.apply(this,arguments)}}(),t}();e.default=o},function(t,e,r){"use strict";var n;(new(((n=r(4))&&n.__esModule?n:{default:n}).default)).start()},function(t,e){!function(t){"use strict";if(!t.fetch){var e={searchParams:"URLSearchParams"in t,iterable:"Symbol"in t&&"iterator"in Symbol,blob:"FileReader"in t&&"Blob"in t&&function(){try{return new Blob,!0}catch(t){return!1}}(),formData:"FormData"in t,arrayBuffer:"ArrayBuffer"in t};if(e.arrayBuffer)var r=["[object Int8Array]","[object Uint8Array]","[object Uint8ClampedArray]","[object Int16Array]","[object Uint16Array]","[object Int32Array]","[object Uint32Array]","[object Float32Array]","[object Float64Array]"],n=function(t){return t&&DataView.prototype.isPrototypeOf(t)},o=ArrayBuffer.isView||function(t){return t&&r.indexOf(Object.prototype.toString.call(t))>-1};c.prototype.append=function(t,e){t=a(t),e=u(e);var r=this.map[t];this.map[t]=r?r+","+e:e},c.prototype.delete=function(t){delete this.map[a(t)]},c.prototype.get=function(t){return t=a(t),this.has(t)?this.map[t]:null},c.prototype.has=function(t){return this.map.hasOwnProperty(a(t))},c.prototype.set=function(t,e){this.map[a(t)]=u(e)},c.prototype.forEach=function(t,e){for(var r in this.map)this.map.hasOwnProperty(r)&&t.call(e,this.map[r],r,this)},c.prototype.keys=function(){var t=[];return this.forEach(function(e,r){t.push(r)}),f(t)},c.prototype.values=function(){var t=[];return this.forEach(function(e){t.push(e)}),f(t)},c.prototype.entries=function(){var t=[];return this.forEach(function(e,r){t.push([r,e])}),f(t)},e.iterable&&(c.prototype[Symbol.iterator]=c.prototype.entries);var i=["DELETE","GET","HEAD","OPTIONS","POST","PUT"];b.prototype.clone=function(){return new b(this,{body:this._bodyInit})},y.call(b.prototype),y.call(v.prototype),v.prototype.clone=function(){return new v(this._bodyInit,{status:this.status,statusText:this.statusText,headers:new c(this.headers),url:this.url})},v.error=function(){var t=new v(null,{status:0,statusText:""});return t.type="error",t};var s=[301,302,303,307,308];v.redirect=function(t,e){if(-1===s.indexOf(e))throw new RangeError("Invalid status code");return new v(null,{status:e,headers:{location:t}})},t.Headers=c,t.Request=b,t.Response=v,t.fetch=function(t,r){return new Promise(function(n,o){var i=new b(t,r),s=new XMLHttpRequest;s.onload=function(){var t,e,r={status:s.status,statusText:s.statusText,headers:(t=s.getAllResponseHeaders()||"",e=new c,t.replace(/\r?\n[\t ]+/g," ").split(/\r?\n/).forEach(function(t){var r=t.split(":"),n=r.shift().trim();if(n){var o=r.join(":").trim();e.append(n,o)}}),e)};r.url="responseURL"in s?s.responseURL:r.headers.get("X-Request-URL");var o="response"in s?s.response:s.responseText;n(new v(o,r))},s.onerror=function(){o(new TypeError("Network request failed"))},s.ontimeout=function(){o(new TypeError("Network request failed"))},s.open(i.method,i.url,!0),"include"===i.credentials?s.withCredentials=!0:"omit"===i.credentials&&(s.withCredentials=!1),"responseType"in s&&e.blob&&(s.responseType="blob"),i.headers.forEach(function(t,e){s.setRequestHeader(e,t)}),s.send(void 0===i._bodyInit?null:i._bodyInit)})},t.fetch.polyfill=!0}function a(t){if("string"!=typeof t&&(t=String(t)),/[^a-z0-9\-#$%&'*+.\^_`|~]/i.test(t))throw new TypeError("Invalid character in header field name");return t.toLowerCase()}function u(t){return"string"!=typeof t&&(t=String(t)),t}function f(t){var r={next:function(){var e=t.shift();return{done:void 0===e,value:e}}};return e.iterable&&(r[Symbol.iterator]=function(){return r}),r}function c(t){this.map={},t instanceof c?t.forEach(function(t,e){this.append(e,t)},this):Array.isArray(t)?t.forEach(function(t){this.append(t[0],t[1])},this):t&&Object.getOwnPropertyNames(t).forEach(function(e){this.append(e,t[e])},this)}function h(t){if(t.bodyUsed)return Promise.reject(new TypeError("Already read"));t.bodyUsed=!0}function d(t){return new Promise(function(e,r){t.onload=function(){e(t.result)},t.onerror=function(){r(t.error)}})}function l(t){var e=new FileReader,r=d(e);return e.readAsArrayBuffer(t),r}function p(t){if(t.slice)return t.slice(0);var e=new Uint8Array(t.byteLength);return e.set(new Uint8Array(t)),e.buffer}function y(){return this.bodyUsed=!1,this._initBody=function(t){if(this._bodyInit=t,t)if("string"==typeof t)this._bodyText=t;else if(e.blob&&Blob.prototype.isPrototypeOf(t))this._bodyBlob=t;else if(e.formData&&FormData.prototype.isPrototypeOf(t))this._bodyFormData=t;else if(e.searchParams&&URLSearchParams.prototype.isPrototypeOf(t))this._bodyText=t.toString();else if(e.arrayBuffer&&e.blob&&n(t))this._bodyArrayBuffer=p(t.buffer),this._bodyInit=new Blob([this._bodyArrayBuffer]);else{if(!e.arrayBuffer||!ArrayBuffer.prototype.isPrototypeOf(t)&&!o(t))throw new Error("unsupported BodyInit type");this._bodyArrayBuffer=p(t)}else this._bodyText="";this.headers.get("content-type")||("string"==typeof t?this.headers.set("content-type","text/plain;charset=UTF-8"):this._bodyBlob&&this._bodyBlob.type?this.headers.set("content-type",this._bodyBlob.type):e.searchParams&&URLSearchParams.prototype.isPrototypeOf(t)&&this.headers.set("content-type","application/x-www-form-urlencoded;charset=UTF-8"))},e.blob&&(this.blob=function(){var t=h(this);if(t)return t;if(this._bodyBlob)return Promise.resolve(this._bodyBlob);if(this._bodyArrayBuffer)return Promise.resolve(new Blob([this._bodyArrayBuffer]));if(this._bodyFormData)throw new Error("could not read FormData body as blob");return Promise.resolve(new Blob([this._bodyText]))},this.arrayBuffer=function(){return this._bodyArrayBuffer?h(this)||Promise.resolve(this._bodyArrayBuffer):this.blob().then(l)}),this.text=function(){var t,e,r,n=h(this);if(n)return n;if(this._bodyBlob)return t=this._bodyBlob,r=d(e=new FileReader),e.readAsText(t),r;if(this._bodyArrayBuffer)return Promise.resolve(function(t){for(var e=new Uint8Array(t),r=new Array(e.length),n=0;n<e.length;n++)r[n]=String.fromCharCode(e[n]);return r.join("")}(this._bodyArrayBuffer));if(this._bodyFormData)throw new Error("could not read FormData body as text");return Promise.resolve(this._bodyText)},e.formData&&(this.formData=function(){return this.text().then(m)}),this.json=function(){return this.text().then(JSON.parse)},this}function b(t,e){var r,n,o=(e=e||{}).body;if(t instanceof b){if(t.bodyUsed)throw new TypeError("Already read");this.url=t.url,this.credentials=t.credentials,e.headers||(this.headers=new c(t.headers)),this.method=t.method,this.mode=t.mode,o||null==t._bodyInit||(o=t._bodyInit,t.bodyUsed=!0)}else this.url=String(t);if(this.credentials=e.credentials||this.credentials||"omit",!e.headers&&this.headers||(this.headers=new c(e.headers)),this.method=(n=(r=e.method||this.method||"GET").toUpperCase(),i.indexOf(n)>-1?n:r),this.mode=e.mode||this.mode||null,this.referrer=null,("GET"===this.method||"HEAD"===this.method)&&o)throw new TypeError("Body not allowed for GET or HEAD requests");this._initBody(o)}function m(t){var e=new FormData;return t.trim().split("&").forEach(function(t){if(t){var r=t.split("="),n=r.shift().replace(/\+/g," "),o=r.join("=").replace(/\+/g," ");e.append(decodeURIComponent(n),decodeURIComponent(o))}}),e}function v(t,e){e||(e={}),this.type="default",this.status=void 0===e.status?200:e.status,this.ok=this.status>=200&&this.status<300,this.statusText="statusText"in e?e.statusText:"OK",this.headers=new c(e.headers),this.url=e.url||"",this._initBody(t)}}("undefined"!=typeof self?self:this)},function(t,e,r){r(6),t.exports=r(5)}]);
//# sourceMappingURL=ridi_token_refresher.js.map