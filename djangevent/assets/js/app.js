'use strict';

var eventsApp = angular.module('EventsApp', ['ngSanitize']);

eventsApp.config(function ($interpolateProvider) {
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
});
