$(document).ready(function(){
    
    var vote_buttons = $('#vote_buttons');
    
    for (var i = 1;i < 6;i++) {
        (function(i) {
            var btn = $('<div class="button noselect">'+i+'</div>');
            vote_buttons.append(btn);
            btn.on('click', function() {
                $.ajax({
                    type: "POST",
                    url: 'http://localhost:7777/widget',
                    data: JSON.stringify({'vote':i})
                });
            });
        })(i);
    }
    
    
});
