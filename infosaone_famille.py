# -*- coding: utf-8 -*-


from osv import osv
from osv import fields

# Doc : http://doc.openerp.com/v6.1/developer/03_modules_2.html

class infosaone_famille(osv.osv):
    _name='infosaone.famille'
    
    #Ordre de tri par defaut des listes
    _order='name'
    
    #ATTENTION : Ne pas mettre d'accent dans le message
    _sql_constraints = [('name_uniq','UNIQUE(name)', 'Ce code existe deja')]    
       
    _columns={
            'name':fields.char("Code",size=20,required=True, select=True),
            'description':fields.text("Description",size=200)
    }   
       
infosaone_famille()



