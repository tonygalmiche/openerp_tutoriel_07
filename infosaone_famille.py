# -*- coding: utf-8 -*-


from osv import osv
from osv import fields

# Doc : http://doc.openerp.com/v6.1/developer/03_modules_2.html


#Remarque : Le nom de la class n'a pas d'importance, mais par convention, mettre le même que le nom du modèle
class infosaone_famille(osv.osv):

    #Nom du modèle à créer
    _name='infosaone.famille'
    
    #Ordre de tri par défaut des listes (Facultatif)
    _order='name'
    
    #Ajoute une contrainte SQL pour empècher la création de doublons (Facultatif)
    #Attention : Ne pas mettre d'accent dans le message
    _sql_constraints = [('name_uniq','UNIQUE(name)', 'Ce code existe deja')]
       
    #Description des 2 champs du modèle
    _columns={
            'name':fields.char("Code",size=20,required=True, select=True),
            'description':fields.text("Description",size=200)
    }   

#Chargement de la class
infosaone_famille()



