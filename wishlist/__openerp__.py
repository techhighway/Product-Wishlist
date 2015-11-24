{
    'name': 'Product Wishlist',
    'category': 'Website',
    'summary': 'Add Products To Wishlist',
    'website': 'https://www.techhighway.co.in',
    'version': '1.0',
    'description': """
OpenERP E-Commerce
==================

        """,
    	'author'	: 'TechHighway Systems Pvt. Ltd.',
	'depends'	: ['website_sale'],
    	'data'	: [
		'views/template.xml',
        	'views/wishlist_template_view.xml',
    		],
    	'qweb'	: ['static/src/xml/*.xml'],
	'images': ['static/description/wishlist_home.png'],	
    	'installable': True,
    	'application': True,
}
