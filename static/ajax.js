function addLike(user_id, profile_id) {
    $.ajax({
        type: 'post',
        url: '/add_like/',
        data: {
            "user_id": user_id,
            "profile_id": profile_id
        },
        success: function (data) {
            console.log(data.data);
            id = 'like_'+data.data.toString();
            document.getElementById(id).innerText = data.like
        }
    });
}


function addComment(user_id, profile_id) {
        $.ajax({
        type: 'post',
        url: '/add_comment/',
        data: {
            "user_id": user_id,
            "profile_id": profile_id,
            "text": document.getElementById('text_comment').value
        },
        success: function (data) {
            console.log(data.comment);
            id = 'comment_'+data.data.toString();
            cur_com = document.getElementById(id).value;
            document.getElementById(id).innerText = cur_com + ', ' + data.comment
        }
    });
}
