/*
	DCAE - js - app:
	@author: mijomir mecu <self@mijomir.com>
*/

function showContact() {
	var c = jQuery('#hb_contact').find('#hbc_wrapper'),
		ci = c.find('#hbc_info');
	c.on('mouseover', function() { ci.show(); }).on('mouseleave', function() { ci.hide(); });
}

function accordion(node) {
	node.find('.accordion_title').each(function(){
		jQuery(this).on('click', function() {
			jQuery(this).parent().siblings().removeClass('expanded').find('.accordion_content').hide();
			jQuery(this).parent().toggleClass('expanded');
			jQuery(this).next().toggle();
		});
	});
}

function animatedScroll(trigger, target) {
	trigger.find('a').each(function() {
		jQuery(this).on('click', function(e){
			e.preventDefault();
			var t = jQuery(this).attr('href'),
				tt = target.find(t);
			jQuery('html, body').animate({scrollTop: tt.offset().top}, 500);
		});
	});
}

jQuery(document).ready(function(){
	if (jQuery('body').hasClass('homepage')) {
		showContact();
	} else if(jQuery('body').hasClass('member')) {
		accordion(jQuery('#m_article'));
	} else if(jQuery('body').hasClass('publications')) {
		accordion(jQuery('.accordion_abstract'));
		animatedScroll(jQuery('#archives'), jQuery('#publications_list'));
		animatedScroll(jQuery('.top_link'), jQuery('#sidebar'));
	} else if(jQuery('body').hasClass('members')) {
		jQuery('.members_role').each(function() {
			jQuery(this).find('.mr_member:first').addClass('alpha')
				.end().find('.mr_member:nth-child(3n+3)').addClass('alpha')
				.end().find('.mr_member:nth-child(3n-1)').addClass('omega').after('<div class="clearfix"></div>');
		});
	}
});
