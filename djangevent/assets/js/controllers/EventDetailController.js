'use strict';

eventsApp.controller('EventDetailController', function EventDetailController($scope, eventsData) {

    $scope.event = eventsData.getEvent(1);

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
