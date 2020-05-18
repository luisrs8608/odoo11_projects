# -*- coding: utf-8 -*-

{
    'name': 'Rating report',
    'summary': 'Shows the customer satisfaction report',
    'version': '11.0.1.0',
    'author': "AITIC",
    'website': 'http://www.aitic.com.ar',
    'license': 'AGPL-3',
    'category': 'Web',
    'depends': ['rating', 'project'],
    # 'depends': ['rating', 'project', 'helpdesk'],
    'description': """
Rating report
=====================================================
1- Rating report

AITIC - Asesoría Integral en IT
=====================================================

""",
    'data': [
        'view/rating_report_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}
