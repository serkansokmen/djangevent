"use strict";

var app = angular.module('DjangularApp', []);

app.config(function ($interpolateProvider) {
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
});

"use strict";

