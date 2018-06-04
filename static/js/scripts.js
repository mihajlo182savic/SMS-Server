
jQuery(document).ready(function() {
	
    /*
        Fullscreen background
    */
   /* $('#home-body').backstretch("img/bg.jpg");*/
	   $.backstretch("/static/img/bg.jpg");
    
    /*
	    Modals
	*/
	$('.launch-modal').on('click', function(e){
		e.preventDefault();
		$( '#' + $(this).data('modal-id') ).modal();
	});
    
    /*
        Form validation
    */
    $('.registration-form input[type="text"], .registration-form textarea').on('focus', function() {
    	$(this).removeClass('input-error');
    });
    
    $('.registration-form').on('submit', function(e) {
    	
    	$(this).find('input[type="text"], textarea').each(function(){
    		if( $(this).val() == "" ) {
    			e.preventDefault();
    			$(this).addClass('input-error');
    		}
    		else {
    			$(this).removeClass('input-error');
    		}
    	});
    	
    });
	
	
	/*
		Show and hide divs when click on radio buttons
	*/
	
	$('.box').hide();
	$('input[type="radio"]').click(function(){
		var valueOfRadio = $(this).attr('value');
		var classOfDivs = $('.'+ valueOfRadio);
		
		$('.box').not(classOfDivs).hide() ; // hide all divs with class box except of classOfDivs
		$(classOfDivs).show();
		
	});   
});
