tinyMCE.init({

	/*
	LANGUAGE_OPTIONS = (
		('ar', u'Arabic'),
		('ar_SA', u'Saudi Arabia'),
		('hy', u'Armenian'),
		('az', u'Azerbaijani'),
		('eu', u'Basque'),
		('be', u'Belarusian'),
		('bn_BD', u'Bengali (Bangladesh)'),
		('bs', u'Bosnian'),
		('bg_BG', u'Bulgarian (Bulgaria)'),
		('bs', u'Bosnian'),
		('ca', u'Catalan'),
		('zh_CN', u'Chinese (China)'),
		('zh_TW', u'Chinese (Taiwan)'),
		('hr', u'Croatian'),
		('cs', u'Czech'),
		('da', u'Danish'),
		('dv', u'Divehi'),
		('nl', u'Dutch'),
		('en_CA', u'English (Canada)'),
		('en_GB', u'English (United Kingdom)'),
		('et', u'Estonian'),
		('fo', u'Faroese'),
		('fi', u'Finnish'),
		('fr_FR', u'French (France)'),
		('gd', u'Gaelic, Scottish'),
		('gl', u'Galician'),
		('ka_GE', u'Georgian (Georgia)'),
		('de', u'German'),
		('de_AT', u'German (Austria)'),
		('el', u'Greek'),
		('he_IL', u'Hebrew (Israel)'),
		('hu_HU', u'Hungarian (Hungary)'),
		('is_IS', u'Icelandic (Iceland)'),
		('id', u'Indonesian'),
		('it', u'Italian'),
		('ja', u'Japanese'),
		('kk', u'Kazakh'),
		('km_KH', u'Khmer (Cambodia)'),
		('ko_KR', u'Korean (Korea)'),
		('lv', u'Latvian'),
		('lt', u'Lithuanian'),
		('lb', u'Luxembourgish'),
		('ml', u'Malayalam'),
		('ml_IN', u'Malayalam (India)'),
		('mn_MN', u'Mongolian (Mongolia)'),
		('nb_NO', u'Norwegian Bokmål (Norway)'),
		('fa', u'Persian'),
		('pl', u'Polish'),
		('pt_BR', u'Portuguese (Brazil)'),
		('pt_PT', u'Portuguese (Portugal)'),
		('ro', u'Romanian'),
		('ru', u'Russian'),
		('sr', u'Serbian'),
		('si_LK', u'Sinhala (Sri Lanka)'),
		('sk', u'Slovak'),
		('sl_SI', u'Slovenian (Slovenia)'),
		('es', u'Spanish'),
		('sv_SE', u'Swedish (Sweden)'),
		('tg', u'Tajik'),
		('ta', u'Tamil'),
		('ta_IN', u'Tamil (India)'),
		('tt', u'Tatar'),
		('th_TH', u'Thai (Thailand)'),
		('tr_TR', u'Turkish (Turkey)'),
		('ug', u'Uighur'),
		('uk', u'Ukrainian'),
		('uk_UA', u'Ukrainian (Ukraine)'),
		('vi', u'Vietnamese'),
		('vi_VN', u'Vietnamese (Viet Nam)'),
		('ci', u'Welsh'),
	)
	 * */

	/*
	Other options

	auto_focus: "elm1",
	directionality : 'ltr',
	external_plugins: {
		"myplugin": "/myplugins/myplugin.js"
	},
	nowrap : false,
	object_resizing : true,
	skin : 'lightgray',
	skin_url: '/css/mytinymceskin',
	theme : 'modern',
	theme_url: '/mytheme/mytheme.js',

	// pentru inlines
	inline : true,
	selector : 'div#edit',
	hidden_input: false


	convert_fonts_to_spans : false,
	entities : "160,nbsp,162,cent,8364,euro,163,pound",
	entity_encoding : "raw",
	extended_valid_elements : "img[class|src|border=0|alt|title|hspace|vspace|width|height|align|onmouseover|onmouseout|name]"
	invalid_elements : "strong,em"
	force_hex_style_colors : true,
	forced_root_block_attrs: {
		"class": "myclass",
		"data-something": "my data"
	},
	indentation : '30px',
	keep_styles: true
	protect: [
		/\<\/?(if|endif)\>/g, // Protect <if> & </endif>
		/\<xsl\:[^>]+\>/g, // Protect <xsl:...>
		/<\?php.*?\?>/g // Protect php code

	]
	body_id: "elm1=my_id,elm2=my_id2",
	body_class: "elm1=my_class,elm2=my_class"
	visual: false,
	visual_table_class: "my-custom-class"
	visual_anchor_class: "my-custom-class"



	**/



	language : 'ro',
	language_url : '/static/admin/tinymce/langs/ro.js',
	custom_undo_redo_levels: 10,

	plugins : 'advlist autolink charmap code contextmenu directionality fullscreen hr importcss insertdatetime link lists nonbreaking paste print preview searchreplace spellchecker table textcolor visualblocks visualchars wordcount',


	browser_spellcheck : true,
	contextmenu : '',
	insertdatetime_formats : ['%d.%m.%Y, %H:%M'],
	nonbreaking_force_tab: true,
	fix_list_elements : true,
	forced_root_block : 'p',
	paste_as_text : true,
	paste_word_valid_elements : 'b,strong,i,em,h1,h2,h3,h4,h5,h6',
	target_list: [
		{title: 'None', value: ''},
		{title: 'Same page', value: '_self'},
		{title: 'New page', value: '_blank'}
	],

	selector: 'textarea',

	element_format : 'html',
	schema: 'html5',
	entities : '38,amp,162,169,copy,60,lt,62,gt',


	// Elements
	valid_elements: '@[id|class|style|title|dir<ltr?rtl|lang|onclick|ondblclick|'
	+ 'onmousedown|onmouseup|onmouseover|onmousemove|onmouseout|onkeypress|'
	+ 'onkeydown|onkeyup],a[rel|rev|charset|hreflang|tabindex|accesskey|type|'
	+ 'name|href|target|title|class|onfocus|onblur],strong/b,em/i,strike,u,'
	+ '#p,-ol[type|compact],-ul[type|compact],-li,br,img[longdesc|usemap|'
	+ 'src|border|alt=|title|hspace|vspace|width|height|align],-sub,-sup,'
	+ '-blockquote,-table[border=0|cellspacing|cellpadding|width|frame|rules|'
	+ 'height|align|summary|bgcolor|background|bordercolor],-tr[rowspan|width|'
	 + 'height|align|valign|bgcolor|background|bordercolor],tbody,thead,tfoot,'
	 + '#td[colspan|rowspan|width|height|align|valign|bgcolor|background|bordercolor'
	 + '|scope],#th[colspan|rowspan|width|height|align|valign|scope],caption,-div,'
	 + '-span,-code,-pre,address,-h1,-h2,-h3,-h4,-h5,-h6,hr[size|noshade],-font[face'
	 + '|size|color],dd,dl,dt,cite,abbr,acronym,del[datetime|cite],ins[datetime|cite],'
	 + 'object[classid|width|height|codebase|*],param[name|value|_value],embed[type|width'
	 + '|height|src|*],script[src|type],map[name],area[shape|coords|href|alt|target],bdo,'
	 + 'button,col[align|char|charoff|span|valign|width],colgroup[align|char|charoff|span|'
	 + 'valign|width],dfn,fieldset,form[action|accept|accept-charset|enctype|method],'
	 + 'input[accept|alt|checked|disabled|maxlength|name|readonly|size|src|type|value],'
	 + 'kbd,label[for],legend,noscript,optgroup[label|disabled],option[disabled|label|selected|value],'
	 + 'q[cite],samp,select[disabled|multiple|name|size],small,'
	 + 'textarea[cols|rows|disabled|name|readonly],tt,var,section,nav,article,aside,header,footer,main,figure.figcaption,data,time,mark,ruby,rt,rp,bdi,wbr',
	 extended_valid_elements : 'embed[width|height|name|flashvars|src|bgcolor|align|play|'
	 + 'loop|quality|allowscriptaccess|type|pluginspage]',

	width: '90%',
	height: 150,

	formats : {
		alignleft : {selector : 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', classes : 'left'},
		aligncenter : {selector : 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', classes : 'center'},
		alignright : {selector : 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', classes : 'right'},
		alignfull : {selector : 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', classes : 'full'},
		bold : {inline : 'span', 'classes' : 'bold'},
		italic : {inline : 'span', 'classes' : 'italic'},
		underline : {inline : 'span', 'classes' : 'underline', exact : true},
		strikethrough : {inline : 'del'},
		forecolor : {inline : 'span', classes : 'forecolor', styles : {color : '%value'}},
		hilitecolor : {inline : 'span', classes : 'hilitecolor', styles : {backgroundColor : '%value'}},
		custom_format : {block : 'h1', attributes : {title : 'Header'}, styles : {color : '%value'}}
	},

	font_formats: 'Arial=arial,helvetica,sans-serif;'+
		'Helvetica=helvetica,arial,sans-serif;'+
		'Palatino=palatino linotype, palatino, book antiqua,urw palladio l;'+
		'Georgia=georgia,palatino;'+
		'Times New Roman=times new roman,times;'+
		'Tahoma=tahoma,arial,helvetica,sans-serif;'+
		'Trebuchet MS=trebuchet ms,geneva;'+
		'Verdana=verdana,geneva;'+
		'Arial Black=arial black,avant garde;'+
		'Impact=impact,chicago;'+
		'Courier New=courier new,courier;'+
		'Symbol=symbol;'+
		'Webdings=webdings;'+
		'Wingdings=wingdings,zapf dingbats',

	 style_formats: [
		{title: 'Paragraph Small', block : 'p', classes: 'p_small'},
		{title: 'Paragraph ImageCaption', block : 'p', classes: 'p_caption'},
		{title: 'Clearfix', block : 'p', classes: 'clearfix'},
		{title: 'Code', block : 'p', classes: 'code'}
	],

	fontsize_formats: '8pt 9pt 10pt 11pt 12pt 13pt 14pt 15px 16pt 18pt 20pt 24pt 26pt 30pt 32pt 36pt 72pt',

	allow_script_urls : false,

	menubar : false,
	statusbar : true,
	resize: 'both',

	toolbar1 : 'bold italic underline strikethrough | hr | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | blockquote | subscript superscript',
	toolbar2 : 'copy cut paste | undo redo | link unlink | charmap | pastetext | removeformat print preview spellchecker searchreplace visualblocks visualchars code fullscreen inserttime',
	toolbar3 : 'fontselect fontsizeselect | forecolor backcolor ltr rtl table',

	content_css : '/static/css/s.css' // resolved to http://domain.mine/mycontent.css

});
