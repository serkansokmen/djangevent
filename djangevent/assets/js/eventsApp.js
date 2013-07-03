'use strict';

var eventsApp = angular.module('EventsApp', ['$strap.directives']);

eventsApp.config(function ($interpolateProvider) {
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
});
