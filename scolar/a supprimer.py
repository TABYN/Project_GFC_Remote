def depence_create_view(request):

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Depence_CreateForm(request, request.POST)
     
     
       
        # check whether it's valid:
        if form.is_valid():
           
     
           
            try:
                # process the data in form.cleaned_data as required
                data=form.cleaned_data
               

                engagement_=Engagement.objects.create(
                    type=data['type'],
                    num=data['num'],
                    date=data['date'],
                    #observation=data['observation'],
                    annee_budg=data['annee_budg'],
     
                    credit_alloue=data['credit_alloue'],
                    montant_operation=data['montant_operation'],
                    fournisseur=data['fournisseur'],
                    facture=data['facture']
                   
                    )  
                credit_reste_s2=Credit_S2.objects.get(pk=engagement_.credit_alloue.id).credit_reste
                credit_S2_=Credit_S2.objects.get(pk=engagement_.credit_alloue.id)
                credit_S2_.credit_reste.amount =credit_reste_s2.amount - engagement_.montant_operation.amount
                assert credit_S2_.credit_reste.amount >= 0
                credit_S2_.save(update_fields=['credit_reste'])  
                   
       
   
            except Exception:
               
               
                if AssertionError:
                    messages.error(request, "ERREUR: Veuillez verifier le montant introduit sachant que le reste comme credit pour cet article : "
                                + str(credit_reste_s2.amount) + "DZD" )          
                    return render(request, 'scolar/create.html', {'form': form })
                elif settings.DEBUG:
                    raise Exception
                else:
                    messages.error(request, "ERREUR: lors de la crÃ©ation de la depence. Veuillez le signaler Ã  l'administrateur.")
                    return render(request, 'scolar/create.html', {'form': form })

            return HttpResponseRedirect(reverse('Depence_List'))




@login_required
def CreditDelete(request,avc, art):
    pavc= Avance.objects.get(pk=avc)
    credit = Credit.objects.get(article=art,avance=avc)
    cpt_bord_liees= Bordereau.objects.filter(credit_id=credit).count()
    exe= pavc.exercice
    
    article = Article.objects.all()
    crdt = Credit.objects.all()
    delete = 3
    if request.method == "POST":
        if cpt_bord_liees>0 : 
             messages.error(request,  "Vous ne pouvez pas supprimer ce credit , des borderaux sont deja liee")
        else :
            credit.delete()
            messages.success(request, 'Credit supprimee definitivement')
            messages.success(request, 'Il reste comme credit Non alloue : ' + str(
             
            pavc.credit_non_allouee.amount + (credit.credit_allouee.amount)) + "DZD")
                            
            pavc.credit_non_allouee.amount = pavc.credit_non_allouee.amount + (credit.credit_allouee.amount)
            pavc.save(update_fields=['credit_non_allouee'])
            
            
            
            
            return render(request, 'scolar/add_credit.html', {'article': article, 'crdt': crdt,'pavc':pavc, 'exe':exe })
    return render(request, 'scolar/delete_item.html', {'delete': delete ,'pavc':pavc,'exe':exe })
                   
       