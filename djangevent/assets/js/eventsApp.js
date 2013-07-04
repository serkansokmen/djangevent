'use strict';

var eventsApp = angular.module('EventsApp', ['ui.bootstrap']);

eventsApp.config(function ($interpolateProvider) {
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
});
