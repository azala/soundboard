$(document).ready(function(){
    
    function play(n) {
        var audio = $('audio');
        audio.attr('src', n+'.mp3');
        audio[0].play();
    }
    
    ws = new WebSocket("ws://localhost:7777/audio");
    
    ws.onopen = function(e) {
        $('#message').text('Connected!');
    }
    
    ws.onmessage = function(e) {
        var d = JSON.parse(e.data);
        if (d.m == 'play') {
            play(d.number);
        }
    }
    
});
