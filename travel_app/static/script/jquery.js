 /*base_page */
$(document).ready(function() {

/*Інформація про сайт*/
	$('#about_site_button').click(function() {
		$('#about_site_info').slideDown(1000); 
	});

	$('#close_about_site').click(function() {
		$('#about_site_info').slideUp(700);
	});

});

/* *** */

	/*home_page*/
$(document).ready(function() {

/*Ефекти обкладинок альбомів*/
	$('div:has(img):nth-child(even)').slideDown(1000);
	$('div:has(img):nth-child(odd)').fadeIn(3500);
	$('div:has(p.p_text)').fadeIn(15000);
	
/*Частково прихована галерея*/
	$('#galery_button').click(function() {

		let height =$('#galery').height();
		let position = $('#galery_button').position();
		let top = position.top;
		let x = 155;

		new_height = height + x + 'px';
		new_comments_height = height + x +100+ 'px';

		new_top = top + x + 'px';
		new_scroll = top;

		$('#galery').css({'height': new_height})
		&& $(this).css({'top': new_top})
		&& $('#users_comments').css({'height': new_comments_height});
/*		&& $(window).scrollTop(new_scroll);
*/	
});


});
/* *** */

	/* add_travel_page */
$(document).ready(function() {
	var $form_travel = $('.form_travel');
	var $input_fields = $('.r1, .r2, .r3, .r4, .r5, .r6');
	var $input_fields_hide = $('.r1, .r2, .r3, .r4, .r5');

	var $label_photo = $('#label_photo');
	var $author_photo = $('#author_photo');

	var $label_travel_name = $('#label_travel_name');
	var $input_travel_name = $('#input_travel_name');

	var $label_travel_route = $('#label_travel_route');
	var $input_travel_route = $('#input_travel_route');

	var $label_travel_cover = $('#label_cover');
	var $input_travel_cover = $('#travel_cover');

	var $label_description = $('#label_description');
	var $input_travel_description = $('#input_travel_description');

	var $r5 = $('.r5');


/*показати форму*/
	
	/*$('#add_data').click(function() {
		$input_fields.slideDown(2000);
	});*/

/*приховати форму*/

	$('#cancel_button').click(function() {
		$input_fields.addClass($input_fields_hide, 3000);
	});
	
/*Зменшення розміру підпису поля input for add_travel page*/
	$input_travel_name.focus(function() {
		$label_travel_name.addClass('label_form_focus')
	});

	$input_travel_route.focus(function() {
		$label_travel_route.addClass('label_form_focus')
	});

	$input_travel_description.focus(function() {
		$label_description.addClass('label_form_focus')
	});


/*Відправка даних*/

	$('#send_button').click(function() {
		if ($('#author_photo').val() != '' 
			&& $('#input_travel_name').val() != '' 
			&& $('#input_travel_description').val() != ''
			&& $('#input_travel_cover').val() != '') {
			$('#form_travel_id').submit(function() {

			$author_photo.addClass('data_input_send').fadeOut(100)
			$label_photo.addClass('label_form_small').addClass('label_form_send').fadeOut(200)

			$input_travel_name.addClass('data_input_small').addClass('data_input_send').fadeOut(500)
			$label_travel_name.addClass('label_form_small').addClass('label_form_send').fadeOut(700)

			$input_travel_route.addClass('data_input_small').addClass('data_input_send').fadeOut(900)
			$label_travel_route.addClass('label_form_small').addClass('label_form_send').fadeOut(1100)

			$input_travel_cover.addClass('data_input_small').addClass('data_input_send').fadeOut(1300)
			$label_travel_cover.addClass('label_form_small').addClass('label_form_send').fadeOut(1000)

			$input_travel_description.addClass('data_input_small').addClass('data_input_send').fadeOut(1400)
			$label_description.addClass('label_form_small').addClass('label_form_send').fadeOut(1100)

			$('.btn_form').addClass('data_input_small').addClass('data_input_send').addClass('button').fadeOut(300)

			});
		} /*end if*/
		
	});

/*	$input_travel_name.focus(function() {
		$label_travel_name.animate({'font-size': '10px', 
									'font-weight': '100',
									'color': '#ff4d4d',
									}, 1000);
		});*/
	

});
/* *** */



	/* add_respond_page */
$(document).ready(function() {

	$('#respond_text').focus();


	$('#respond_text').click(function() {
		$('#label_textarea').addClass('label_form_focus')
	});

	$('#respond_text').keydown(function() {
		$('#label_textarea').addClass('label_form_focus')
	});


	$('#datetimepicker').focus(function() {
		$('#label_datepicker').addClass('label_form_focus')
	});


});
/* *** */


	/*show_photo_page*/
$(document).ready(function() {
	$('.img_big').fadeOut(1);

	$('#close_travel_info').click(function() {
		$(this).fadeOut(700)
			&& $('#close_travel_info_hr').fadeOut(800)
			&& $('.travel_info').slideUp(1000)
			&& $('.img_big').fadeIn(4000)
			&& $('#read_travel_description').fadeIn(6000)
			&& $('#show_travel_info').fadeIn(8000);
	});

	$('#show_travel_info').click(function() {

		$(this).fadeOut(1000) 
		&& $('.travel_info').slideDown(1000)
		&& $('#close_travel_info_hr').fadeIn(800)
		&& $('.img_big').fadeOut(2000)
		&& $('#read_travel_description').fadeOut(300)
		&& $('#close_travel_info').fadeIn(300)
		&& $('#travel_description').slideUp(700);
	});

	$('#read_travel_description').click(function() {
		$(this).fadeOut(1000)
		$('.img_big').fadeOut(1000)
		&& $('#travel_description').slideDown(2000);
	});

	$('#close_description').click(function() {
		$('#travel_description').slideUp(1000)
		&& $('.img_big').fadeIn(2000)
		&& $('#read_travel_description').fadeIn(3000);
	});

/*Показати велике зображення*/
	$('img').click(function() {
		
	});

});

/* *** */


	/*plan_trip_page*/

/*стилі форми*/
$(document).ready(function() {

	$('#trip_point_input').focus(function() {
		$('#trip_point_label').addClass('label_form_focus')
	});

	$('#trip_description_input').focus(function() {
		$('#trip_description_label').addClass('label_form_focus')
	});

	$('#number_of_seats_input').focus(function() {
		$('#number_of_seats_label').addClass('label_form_focus')
	});

	$('#departure_date_input').focus(function() {
		$('#departure_date_label').addClass('label_form_focus')
	});

	$('#date_of_arrival_input').focus(function() {
		$('#date_of_arrival_label').addClass('label_form_focus')
	});




/*Відправка даних*/
/*	if ($('.trip_point_input') != ''
		&& $('#trip_description_input') != ''
		&& $('#number_of_sets_input') != ''
		&& $('#departure_date_input') != ''
		&& $('#date_of_arrival_input') != '') {
		$('#plan_trip_form').submit(function() {
			$('#trip_point_input').click(function() {

				$('#trip_point_label').

			});
		});
	}

	
*/
});

/* *** */

		/*to_join_the_trip_page*/

	$(document).ready(function() {

		if ($.isNumeric($('.trip_info').find('input').val())) {

			$('#seats_info_p').css({'color': 'green'}) &&
			$('#to_join_form').fadeIn(1000);

		} else {

			$('#seats_info_p').css({'color': 'red'});
		}


		$('#first_name_input').click(function() {
			$('#first_name_label').addClass('label_form_focus');
		});

		$('#last_name_input').click(function() {
			$('#last_name_label').addClass('label_form_focus');
		});

	});




/* *** */


		/* plan_trip_page */

	$(document).ready(function() {
		$('#trip_point_input').focus();
	});

/* *** */

