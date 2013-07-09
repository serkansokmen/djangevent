'use strict';

eventsApp.controller('EventDetailController', function EventDetailController($scope, eventsData, $routeParams) {

    $scope.event = eventsData.getEvent($routeParams.eventId);

    $scope.event.then(
        function (event) { console.log(event); },
        function (response) { console.log(response); }
    );

    $scope.sortOrder = 'name';

    $scope.upVoteSession = function (session) {
        session.voteCount++;
    };
    $scope.downVoteSession = function (session) {
        session.voteCount--;
    };
});
