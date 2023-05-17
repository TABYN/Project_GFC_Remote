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
                    messages.error(request, "ERREUR: lors de la cr√©ation de la depence. Veuillez le signaler √  l'administrateur.")
                    return render(request, 'scolar/create.html', {'form': form })

            return HttpResponseRedirect(reverse('Depence_List'))
                   
       