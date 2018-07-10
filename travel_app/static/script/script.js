function initAlbumSelector() {

	$('#galery>.albums_covers').click(function(event) {

		/*Отримуємо знч. обраного тегу*/
		var album = $(this).find('input').val();
	
		if (album) {
			$.cookie('current_album', album, {'path': '/', 'expires': 365});
		} else {
			$.removeCookie('current_album', {'path': '/'});
		}

		return true;


	});
}

function initTripSelector() {
	$('.trip_list>.trip_div').click(function () {
		var trip_id = $(this).find('input').val();
		console.log('input.val - ', trip_id);

		if (trip_id) {
			$.cookie('current_trip', trip_id, {'path': '/to_join_the_trip', 'expires': 365});	
		} else {
			$.removeCookie('current_trip', {'path': '/to_join_the_trip'});
		}

		return true;
			});
}

function initDateFields() {
	
	$('.dateinput').datetimepicker({
		'format': 'YYYY-MM-DD'
		
	}).on('dp.hide', function(event) {
		$(this).blur();
	});
}


$(document).ready(function() {
	initAlbumSelector();
	initTripSelector();
	initDateFields();

});