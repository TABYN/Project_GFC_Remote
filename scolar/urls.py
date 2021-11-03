from django.urls import  path, re_path, include
#from django.views import generic
from wkhtmltopdf.views import PDFTemplateView

from scolar import views

#handler404 = 'scolar.views.page_not_found_view'

urlpatterns = [
    re_path(r'^select2/', include('django_select2.urls')),
    re_path(r'^competence_list/$', views.competence_list_view, name='competence_list'),
    re_path(r'^referentiel_competence/$', views.ReferentielCompetenceView.as_view(), name='referentiel_competence'),
    re_path(r'^matrice_competence_ddc/$', views.MatriceCompetenceDDCView.as_view(), name='matrice_competence_ddc'),
    re_path(r'^matrice_competence_niveau/$', views.MatriceCompetenceNiveauView.as_view(), name='matrice_competence_niveau'),
    re_path(r'^catalogue_programme/$', views.CatalogueProgrammeView.as_view(), name='catalogue_programme'),
    re_path(r'^competence_family_list/$', views.CompetenceFamilyListView.as_view(), name='competence_family_list'),
    re_path(r'^competence_family_create/$', views.CompetenceFamilyCreateView.as_view(), name='competence_family_create'),
    re_path(r'^competence_family_update/(?P<pk>\w+)/$', views.CompetenceFamilyUpdateView.as_view(), name='competence_family_update'),
    re_path(r'^competence_family_delete/(?P<pk>\w+)/$', views.CompetenceFamilyDeleteView.as_view(), name='competence_family_delete'),
    re_path(r'^competence_list/(?P<competence_family_pk>\w+)/$', views.CompetenceListView.as_view(), name='competence_list'),
    re_path(r'^competence_create/(?P<competence_family_pk>\w+)/$', views.CompetenceCreateView.as_view(), name='competence_create'),
    re_path(r'^competence_update/(?P<pk>\d+)/(?P<competence_family_pk>\w+)/$', views.CompetenceUpdateView.as_view(), name='competence_update'),
    re_path(r'^competence_delete/(?P<pk>\d+)/(?P<competence_family_pk>\w+)/$', views.CompetenceDeleteView.as_view(), name='competence_delete'),
    re_path(r'^competence_element_list/(?P<competence_pk>\d+)/$', views.CompetenceElementListView.as_view(), name='competence_element_list'),
    re_path(r'^competence_element_create/(?P<competence_pk>\d+)/$', views.CompetenceElementCreateView.as_view(), name='competence_element_create'),
    re_path(r'^competence_element_update/(?P<pk>\d+)/(?P<competence_pk>\d+)/$', views.CompetenceElementUpdateView.as_view(), name='competence_element_update'),
    re_path(r'^competence_element_delete/(?P<pk>\d+)/(?P<competence_pk>\d+)/$', views.CompetenceElementDeleteView.as_view(), name='competence_element_delete'),
    path('dashboard_etudiant', views.DashboardEtudiantView.as_view(), name='dashboard_etudiant'),
    path('dashboard_enseignant', views.DashboardEnseignantView.as_view(), name='dashboard_enseignant'),
    path('dashboard_formation', views.DashboardFormationView.as_view(), name='dashboard_formation'),
    re_path(r'^import_deliberation/(?P<annee_univ_pk>\d{4})/$$', views.import_deliberation_view, name='import_deliberation'),
    re_path(r'^deliberation_list/$', views.DeliberationListView.as_view(), name='deliberation_list'),
    re_path(r'^deliberation_detail/(?P<formation_pk>\d+)/$', views.DeliberationDetailView.as_view(), name='deliberation_detail'),
    re_path(r'^confirmer_deliberation/(?P<formation_pk>\d+)/$', views.confirmer_deliberation_view, name='confirmer_deliberation'),
#    re_path(r'^deliberation_annuelle/(?P<formation_pk>\d+)/(?P<photo>\d{1})/(?P<sort>\d{1})/(?P<signatures>\d{1})/$', views.DeliberationAnnuelleView.as_view(), name='deliberation_annuelle'),
    re_path(r'^deliberation_annuelle_settings/(?P<formation_pk>\d+)/$', views.deliberation_annuelle_settings_view, name='deliberation_annuelle_settings'),
#    re_path(r'^deliberation_pdf/(?P<formation_pk>\d+)/(?P<photo>\d{1})/(?P<periode_pk>\d+)/(?P<sort>\d{1})/$', views.DeliberationPDFView.as_view(), name='deliberation_pdf'),
#    re_path(r'^deliberation_provisoire_pdf/(?P<formation_pk>\d+)/(?P<periode_pk>\d+)$', views.DeliberationProvisoirePDFView.as_view(), name='deliberation_provisoire_pdf'),
#    re_path(r'^deliberation_provisoire/(?P<formation_pk>\d+)/(?P<periode_pk>\d+)$', views.DeliberationProvisoireView.as_view(), name='deliberation_provisoire'),
    re_path(r'^deliberation_provisoire_settings/(?P<formation_pk>\d+)/(?P<periode_pk>\d+)/$', views.deliberation_provisoire_settings_view, name='deliberation_provisoire_settings'),
#    re_path(r'^deliberation_etudiants_pdf/(?P<formation_pk>\d+)/(?P<periode_pk>\d+)/$', views.DeliberationEtudiantsPDFView.as_view(), name='deliberation_etudiants_pdf'),
    re_path(r'^deliberation_calcul/(?P<formation_pk>\d+)/$', views.deliberation_calcul_view, name='deliberation_calcul'),
#    re_path(r'^deliberation_periode_calcul/(?P<formation_pk>\d+)/(?P<periode_pk>\d+)/$', views.deliberation_periode_calcul_view, name='deliberation_periode_calcul'),
    re_path(r'^pv_detail/(?P<pk>\d+)/$', views.PVDetailView.as_view(), name='pv_detail'),
    re_path(r'^pv_list/$', views.PVListView.as_view(), name='pv_list'),
    re_path(r'^export_pv/(?P<formation_pk>\d+)/$', views.export_pv_view, name='export_pv'),
    re_path(r'^pv_delete/(?P<pk>\d+)/$', views.PVDeleteView.as_view(), name='pv_delete'),
    #re_path(r'^deliberation_update/(?P<formation_pk>\d+)/$', views.deliberation_update_view, name='deliberation_update'),
    re_path(r'^note_eliminatoire_update/(?P<formation_pk>\d+)/$', views.note_eliminatoire_update_view, name='note_eliminatoire_update'),
    re_path(r'^notes_eliminatoires_pv_pdf/(?P<formation_pk>\d+)/(?P<periode_pk>\d+)/$', views.NotesEliminatoiresPVPDFView.as_view(), name='notes_eliminatoires_pv_pdf'),
    re_path(r'^notes_eliminatoires_pv_provisoire_pdf/(?P<formation_pk>\d+)/(?P<periode_pk>\d+)/$', views.NotesEliminatoiresPVProvisoirePDFView.as_view(), name='notes_eliminatoires_pv_provisoire_pdf'),
    re_path(r'^feedback_module_pdf/(?P<module_pk>\d+)/$', views.FeedbackModulePDFView.as_view(), name='feedback_module_pdf'),
    re_path(r'^document_list/$', views.document_list_view, name='document_list'),
    re_path(r'^releve_notes/(?P<inscription_pk>\d+)/$', views.ReleveNotesView.as_view(), name='releve_notes'),
    re_path(r'^releve_notes_update/(?P<inscription_pk>\d+)/$', views.releve_notes_update_view, name='releve_notes_update'),
    re_path(r'^notes_clear/(?P<inscription_periode_pk>\d+)/$', views.notes_clear_view, name='notes_clear'),
    re_path(r'^acquis_clear/(?P<resultat_pk>\d+)/$', views.acquis_clear_view, name='acquis_clear'),
    re_path(r'^modules_acquis/(?P<inscription_pk>\d+)/$', views.modules_acquis_view, name='modules_acquis'),
    
    re_path(r'^releve_notes_pdf/(?P<inscription_pk>\d+)/(?P<signature>\d{1})/$', views.ReleveNotesPDFView.as_view(), name='releve_notes_pdf'),
    re_path(r'^releve_notes_global_pdf/(?P<etudiant_pk>\d{2}/\d{4})/(?P<diplome_pk>\d+)/$', views.ReleveNotesGlobalPDFView.as_view(), name='releve_notes_global_pdf'),
    #re_path(r'^releve_notes_list_pdf/(?P<formation_pk>\d+)/(?P<periode_pk>\d+)/$', views.ReleveNotesListPDFView.as_view(), name='releve_notes_list_pdf'),
    #re_path(r'^releve_notes_list_pdf/(?P<formation_pk>\d+)/$', views.ReleveNotesListPDFView.as_view(), name='releve_notes_list_pdf'),
    re_path(r'^releve_notes_list_pdf/(?P<formation_pk>\d+)/(?P<periode_pk>\d+)/$', views.releve_notes_list_pdf_view, name='releve_notes_list_pdf'),
    re_path(r'^releve_notes_provisoire_pdf/(?P<inscription_pk>\d+)/(?P<periode_pk>\d+)/(?P<signature>\d{1})/$', views.ReleveNotesProvisoirePDFView.as_view(), name='releve_notes_provisoire_pdf'),
    re_path(r'^releve_notes_provisoire_list_pdf/(?P<formation_pk>\d+)/(?P<periode_pk>\d+)/$', views.ReleveNotesProvisoireListPDFView.as_view(), name='releve_notes_provisoire_list_pdf'),
    re_path(r'^releve_ects_pdf/(?P<inscription_pk>\d+)/(?P<signature>\d{1})/$', views.ReleveECTSPDFView.as_view(), name='releve_ects_pdf'),
    re_path(r'^releve_ects/(?P<inscription_pk>\d+)/$', views.ReleveECTSView.as_view(), name='releve_ects'),
    re_path(r'^releve_ects_list_pdf/(?P<formation_pk>\d+)/(?P<periode_pk>\d+)/$', views.ReleveECTSListPDFView.as_view(), name='releve_ects_list_pdf'), 
    re_path(r'^certificat_pdf/(?P<inscription_pk>\d+)/(?P<signature>\d{1})/$', views.CertificatPDFView.as_view(), name='certificat_pdf'),
    re_path(r'^fiche_inscription_pdf/(?P<inscription_pk>\d+)/$', views.FicheInscriptionPDFView.as_view(), name='fiche_inscription_pdf'),
    #re_path(r'^certificat_list_pdf/(?P<formation_pk>\d+)/(?P<periode_pk>\d+)/$', views.CertificatListPDFView.as_view(), name='certificat_list_pdf'),
    re_path(r'^certificat_list_pdf/(?P<formation_pk>\d+)/(?P<periode_pk>\d+)/$', views.certificat_3l_list_pdf_view, name='certificat_list_pdf'),
    re_path(r'^certificat_old_pdf/(?P<inscription_pk>\d+)/$', views.CertificatOldPDFView.as_view(), name='certificat_old_pdf'),
    re_path(r'^certificat_conges_pdf/(?P<inscription_pk>\d+)/(?P<signature>\d+)/$', views.CertificatCongesPDFView.as_view(), name='certificat_conges_pdf'),
    #re_path(r'^certificat_old_list_pdf/(?P<formation_pk>\d+)/(?P<periode_pk>\d+)/$', views.CertificatOldListPDFView.as_view(), name='certificat_old_list_pdf'),
    re_path(r'^certificat_old_list_pdf/(?P<formation_pk>\d+)/(?P<periode_pk>\d+)/$', views.certificat_2l_list_pdf_view, name='certificat_old_list_pdf'),
    re_path(r'^pv_pfe_pdf/(?P<groupe_pk>\d+)/(?P<module_pk>\d+)/$', views.PVPFEPDFView.as_view(), name='pv_pfe_pdf'),
    path('pfe_list', views.PFEListView.as_view(), name='pfe_list'),
    path('export_pfe_list', views.export_pfe_list, name='export_pfe_list'),
    re_path(r'^export_etudiant_pfe_list/(?P<formation_pk>\d+)/$', views.export_etudiant_pfe_list, name='export_etudiant_pfe_list'),
    re_path(r'^pfe_create/(?P<organisme_pk>[ -_&@\w]+)/$', views.PFECreateView.as_view(), name='pfe_create'),
    re_path(r'^pfe_update/(?P<pk>\d+)/$', views.PFEUpdateView.as_view(), name='pfe_update'),
    re_path(r'^pfe_delete/(?P<pk>\d+)/$', views.PFEDeleteView.as_view(), name='pfe_delete'),
    re_path(r'^pfe_detail/(?P<pk>\d+)/$', views.PFEDetailView.as_view(), name='pfe_detail'),
    re_path(r'^pfe_fiche_pdf/(?P<pfe_pk>\d+)/$', views.PFEPDFView.as_view(), name='pfe_fiche_pdf'),
    re_path(r'^pfe_fiche_list_pdf/(?P<formation_pk>\d+)/(?P<periode_pk>\d+)/$', views.pfe_fiche_list_pdf_view, name='pfe_fiche_list_pdf'),
    re_path(r'^commission_validation_create/(?P<pfe_pk>\d+)/$', views.commission_validation_create_view, name='commission_validation_create'),
    re_path(r'^validation_update/(?P<pk>\d+)/(?P<pfe_pk>\d+)/$', views.ValidationUpdateView.as_view(), name='validation_update'),
    re_path(r'^validation_delete/(?P<pk>\d+)/(?P<pfe_pk>\d+)/$', views.ValidationDeleteView.as_view(), name='validation_delete'),
    path('enseignant_pfe_list', views.EnseignantPFEListView.as_view(), name='enseignant_pfe_list'),
    path('etudiant_pfe_list', views.EtudiantPFEListView.as_view(), name='etudiant_pfe_list'),
    path('service_pfe_list', views.ServicePFEListView.as_view(), name='service_pfe_list'),
    path('enseignant_expertise_pfe_list', views.EnseignantExpertisePFEListView.as_view(), name='enseignant_expertise_pfe_list'),
    path('experts_index', views.ExpertsIndexView.as_view(), name='experts_index'),
    path('organisme_create_for_pfe_create', views.organisme_create_for_pfe_create, name='organisme_create_for_pfe_create'),
    path('organisme_select_for_pfe_create', views.organisme_select_for_pfe_create, name='organisme_select_for_pfe_create'),
    path('organisme_create', views.OrganismeCreateView.as_view(), name='organisme_create'),
    path('organismes_import', views.organismes_import_view, name='organismes_import'),
    re_path(r'^organisme_update/(?P<pk>[ -_&@\w]+)/$', views.OrganismeUpdateView.as_view(), name='organisme_update'),
    re_path(r'^organisme_delete/(?P<pk>[ -_&@\w]+)/$', views.OrganismeDeleteView.as_view(), name='organisme_delete'),
    path('organisme_list', views.OrganismeListView.as_view(), name='organisme_list'),
    re_path(r'^situation_certificate_pdf/(?P<inscription_pk>\d+)/$', views.EtudiantSituationCertificatePDFView.as_view(), name='situation_certificate_pdf'),
    re_path(r'^attestation_etudes_frances_pdf/(?P<inscription_pk>\d+)/$', views.EtudiantAttestationEtudesFrancaisPDFView.as_view(), name='attestation_etudes_francais_pdf'),
    re_path(r'^inscription_update/(?P<pk>\d+)/$',views.inscription_update_view, name='inscription_update'),
    re_path(r'^inscription_delete/(?P<pk>\d+)/(?P<etudiant_pk>\d{2}/\d{4})/$',views.InscriptionDeleteView.as_view(), name='inscription_delete'),
    re_path(r'^inscription_create/(?P<etudiant_pk>\d{2}/\d{4})/$',views.InscriptionCreateView.as_view(), name='inscription_create'),
    re_path(r'^inscription_annee_suivante/(?P<formation_pk>\d+)/$',views.inscription_annee_suivante_view, name='inscription_annee_suivante'),
    re_path(r'^inscriptions_import/$',views.inscriptions_import_view, name='inscriptions_import'),
    re_path(r'^feedback_periode_detail/(?P<periode_pk>\d+)/(?P<annee_univ_pk>\d{4})/(?P<with_comments>\d{1})/$', views.FeedbackPeriodeView.as_view(), name='feedback_periode_detail'),
    re_path(r'^feedback_etudiant_update/(?P<periode_pk>\d+)/(?P<inscription_pk>\d+)/$', views.feedback_etudiant_update_view, name='feedback_etudiant_update'),
    path('index', views.index, name='index'),
    path('home', views.index, name='home'),
    path('activite', views.ActiviteTableView.as_view(), name='activite'),
    path('activite_soutenance', views.ActiviteSoutenancesView.as_view(), name='activite_soutenance'),
    re_path(r'^activite_create/(?P<groupe_pk>\d+)/(?P<module_pk>\d+)/$',views.ActiviteCreateView.as_view(), name='activite_create'),
    re_path(r'^activite_update/(?P<pk>\d+)/(?P<formation_pk>\d+)/(?P<periode_pk>\d+)/$',views.ActiviteUpdateView.as_view(), name='activite_update'),
    re_path(r'^activite_delete/(?P<pk>\d+)/(?P<formation_pk>\d+)/(?P<periode_pk>\d+)/$',views.ActiviteDeleteView.as_view(), name='activite_delete'),
    path('anneeuniv_list', views.AnneeUnivListView.as_view(), name='anneeuniv_list'),
    path('anneeuniv_create', views.AnneeUnivCreateView.as_view(), name='anneeuniv_create'),
    re_path(r'^anneeuniv_update/(?P<pk>\d{4})/$', views.AnneeUnivUpdateView.as_view(), name='anneeuniv_update'),
    re_path(r'^formation_list/(?P<annee_univ_pk>\d{4})/$',views.FormationListView.as_view(), name='formation_list'),
    re_path(r'^formation_create/(?P<annee_univ_pk>\d{4})/$',views.FormationCreateView.as_view(), name='formation_create'),
    re_path(r'^formation_update/(?P<annee_univ_pk>\d{4})/(?P<pk>\d+)/$',views.FormationUpdateView.as_view(), name='formation_update'),
    re_path(r'^departement_create/$',views.DepartementCreateView.as_view(), name='departement_create'),
    re_path(r'^departement_update/(?P<pk>\d+)/$',views.DepartementUpdateView.as_view(), name='departement_update'),
    re_path(r'^departement_delete/(?P<pk>\d+)/$',views.DepartementDeleteView.as_view(), name='departement_delete'),

    re_path(r'^formation_delete/(?P<pk>\d+)/(?P<annee_univ_pk>\d{4})/$',views.FormationDeleteView.as_view(), name='formation_delete'),
    re_path(r'^formation_archive_toggle/(?P<formation_pk>\d+)/$',views.formation_archive_toggle_view, name='formation_archive_toggle'),
    re_path(r'^section_list/(?P<formation_pk>\d+)/$',views.SectionListView.as_view(), name='section_list'),
    re_path(r'^section_create/(?P<formation_pk>\d+)/$',views.SectionCreateView.as_view(), name='section_create'),
    re_path(r'^section_delete/(?P<pk>\d+)/(?P<formation_pk>\d+)/$',views.SectionDeleteView.as_view(), name='section_delete'),
    re_path(r'^groupe_list/(?P<section_pk>\d+)/$',views.GroupeListView.as_view(), name='groupe_list'),
    re_path(r'^groupe_all_list/$',views.GroupeAllListView.as_view(), name='groupe_all_list'),
    re_path(r'^groupe_create/(?P<section_pk>\d+)/$',views.GroupeCreateView.as_view(), name='groupe_create'),
    re_path(r'^groupe_delete/(?P<pk>\d+)/(?P<section_pk>\d+)/$',views.GroupeDeleteView.as_view(), name='groupe_delete'),
    re_path(r'^groupe_update/(?P<pk>\d+)/(?P<section_pk>\d+)/$',views.GroupeUpdateView.as_view(), name='groupe_update'),
    path('planification_list', views.PlanificationListView.as_view(), name='planification_list'),
    re_path(r'^planification_update/(?P<formation_pk>\d+)/(?P<periode_pk>\d+)/$',views.PlanificationUpdateView.as_view(), name='planification_update'),
    re_path(r'^planning_import_from_fet/$',views.planning_import_from_fet, name='planning_import_from_fet'),
    re_path(r'^from_fet_to_google_agenda/$',views.from_fet_to_google_agenda, name='from_fet_to_google_agenda'),
    re_path(r'^clear_google_agenda/$',views.clear_google_agenda, name='clear_google_agenda'),
    path('etudiants_import', views.etudiants_import_view, name='etudiants_import'),
    path('etudiants_import_maj', views.etudiants_import_maj_view, name='etudiants_import_maj'),
    path('inscription_list',views.InscriptionListView.as_view(),name='inscription_list'),
    path('preinscription_create',views.PreinscriptionCreateView.as_view(),name='preinscription_create'),
    path('preinscription_list',views.PreinscriptionListView.as_view(),name='preinscription_list'),
    re_path(r'^validation_preinscription/(?P<inscription_pk>\d+)/$',views.validation_preinscription_view, name='validation_preinscription'),
    path('public_etudiant_list',views.PublicEtudiantListView.as_view(),name='public_etudiant_list'),
    path('etudiant_list',views.EtudiantListView.as_view(),name='etudiant_list'),
    re_path(r'^etudiant_inscription_list/(?P<etudiant_pk>\d{2}/\d{4})/$',views.EtudiantInscriptionListView.as_view(), name='etudiant_inscription_list'),
    re_path(r'^etudiant_groupe_list/(?P<groupe_pk>\d+)/(?P<periode_pk>\d+)/$',views.EtudiantGroupeListView.as_view(), name='etudiant_groupe_list'),
    re_path(r'^groupe_list_export/(?P<groupe_pk>\d+)/(?P<periode_pk>\d+)/$',views.groupe_list_export_view, name='groupe_list_export'),
    re_path(r'^etudiant_detail/(?P<pk>\d{2}/\d{4})/$',views.EtudiantDetailView.as_view(), name='etudiant_detail'),
    re_path(r'^etudiant_update/(?P<pk>\d{2}/\d{4})/$',views.EtudiantUpdateView.as_view(), name='etudiant_update'),
    re_path(r'^etudiant_profile_update/(?P<pk>\d{2}/\d{4})/$',views.EtudiantProfileUpdateView.as_view(), name='etudiant_profile_update'),
    re_path(r'^etudiant_activite_extra_update/(?P<pk>\d{2}/\d{4})/$',views.EtudiantActiviteExtraUpdateView.as_view(), name='etudiant_activite_extra_update'),
    path('etudiant_activite', views.ActiviteEtudiantTableView.as_view(), name='etudiant_activite'),
    re_path(r'^etudiant_documents_list/(?P<etudiant_pk>\d{2}/\d{4})/$',views.EtudiantDocumentsListView.as_view(), name='etudiant_documents_list'),
    path('edt_list', views.edt_list_view, name='edt_list'),
    path('edt_etudiant', views.EDTEtudiantView.as_view(), name='edt_etudiant'),
    re_path(r'^etudiant_module_absences/(?P<etudiant_pk>\d{2}/\d{4})/(?P<module_pk>\d+)/$',views.AbsenceEtudiantView.as_view(), name='etudiant_module_absences'),
    re_path(r'^etudiant_module_notes/(?P<etudiant_pk>\d{2}/\d{4})/(?P<matiere_pk>\d+)/$',views.NoteEtudiantListView.as_view(), name='etudiant_module_notes'),
    re_path(r'^module_detail/(?P<pk>\d+)/$',views.ModuleDetailView.as_view(), name='module_detail'),
    re_path(r'^module_list/$',views.ModuleListView.as_view(), name='module_list'),
    re_path(r'^module_update/(?P<pk>\d+)/(?P<formation_pk>\d+)/(?P<periode_pk>\d+)/$',views.ModuleUpdateView.as_view(), name='module_update'),
    re_path(r'^module_delete/(?P<pk>\d+)/(?P<formation_pk>\d+)/(?P<periode_pk>\d+)/$',views.ModuleDeleteView.as_view(), name='module_delete'),
    re_path(r'^module_suivi_update/(?P<pk>\d+)/(?P<formation_pk>\d+)/(?P<periode_pk>\d+)/$',views.ModulesSuivisUpdateView.as_view(), name='module_suivi_update'),
    re_path(r'^module_evaluation_copy/(?P<module_pk>\d+)/$',views.module_evaluation_copy_view, name='module_evaluation_copy'),
    re_path(r'^module_suivi_delete/(?P<pk>\d+)/(?P<formation_pk>\d+)/(?P<periode_pk>\d+)/$',views.ModulesSuivisDeleteView.as_view(), name='module_suivi_delete'),
    re_path(r'^module_suivi_create/(?P<module_pk>\d+)/(?P<groupe_pk>\d+)/$',views.ModulesSuivisCreateView.as_view(), name='module_suivi_create'),
    re_path(r'^feedback_list/(?P<module_pk>\d+)/$',views.FeedbackListView.as_view(), name='feedback_list'),
    re_path(r'^feedback_update/(?P<pk>\d+)/(?P<module_pk>\d+)/$',views.FeedbackUpdateView.as_view(), name='feedback_update'),
    re_path(r'^feedback_module_detail/(?P<module_pk>\d+)/$',views.FeedbackModuleView.as_view(), name='feedback_module_detail'),
    re_path(r'^import_feedback_module/(?P<module_pk>\d+)/$',views.feedback_import_view, name='import_feedback_module'),
    re_path(r'^assiduite/(?P<activite_pk>\d+)/$',views.SeanceTableView.as_view(), name='assiduite'),
    re_path(r'^absence_list/$',views.AbsenceEtudiantListView.as_view(), name='absence_list'),
    re_path(r'^absence_seance_list/(?P<seance_pk>\d+)/(?P<activite_pk>\d+)/$',views.AbsenceEtudiantSeanceListView.as_view(), name='absence_seance_list'),
    path('signaler_absence_etudiant',views.signaler_absence_etudiant, name='signaler_absence_etudiant'),
    path('absence_etudiant_report',views.absence_etudiant_report, name='absence_etudiant_report'),
    re_path(r'^absence_etudiant_delete/(?P<seance_pk>\d+)/(?P<activite_pk>\d+)/(?P<pk>\d+)/$',views.AbsenceEtudiantDeleteView.as_view(), name='absence_etudiant_delete'),
    re_path(r'^absence_update/(?P<pk>\d+)/$',views.AbsenceEtudiantUpdateView.as_view(), name='absence_update'),
    re_path(r'^absence_enseignant_list/$',views.AbsenceEnseignantListView.as_view(), name='absence_enseignant_list'),
    re_path(r'^absence_enseignant_update/(?P<pk>\d+)/$',views.AbsenceEnseignantUpdateView.as_view(), name='absence_enseignant_update'),

    re_path(r'^seance_detail/(?P<seance_pk>\d+)/$',views.SeanceDetailView.as_view(), name='seance_detail'),
    re_path(r'^seance_create/(?P<activite_pk>\d+)/$',views.SeanceCreate.as_view(), name='seance_create'),
    re_path(r'^seance_update/(?P<activite_pk>\d+)/(?P<pk>\d+)/$',views.SeanceUpdateView.as_view(), name='seance_update'),
    re_path(r'^seance_delete/(?P<activite_pk>\d+)/(?P<pk>\d+)/$',views.SeanceDeleteView.as_view(), name='seance_delete'),
    re_path(r'^seance_rattrapage_create/(?P<activite_pk>\d+)/$',views.SeanceRattrapageCreateView.as_view(), name='seance_rattrapage_create'),
    
    re_path(r'^examen_list/$',views.ExamenListView.as_view(), name='examen_list'),
    re_path(r'^pv_examen_list/(?P<seance_pk>\d+)/$',views.PVExamenListView.as_view(), name='pv_examen_list'),
    re_path(r'^examen_create/$',views.examen_create_view, name='examen_create'),
    re_path(r'^examen_delete/(?P<pk>\d+)/$',views.ExamenDeleteView.as_view(), name='examen_delete'),
    re_path(r'^envoi_convocations_examens/$',views.envoi_convocations_examens_view, name='envoi_convocations_examens'),
    re_path(r'^affichage_convocations_examens/$',views.affichage_convocations_examens_view, name='affichage_convocations_examens'),
    re_path(r'^seance_salles_reservation/(?P<seance_pk>\d+)/$',views.seance_salles_reservation, name='seance_salles_reservation'),
    re_path(r'^placer_surveillants_etudiants/(?P<seance_pk>\d+)/$',views.placer_surveillants_etudiants, name='placer_surveillants_etudiants'),
    
    
    re_path(r'^import_notes/$',views.notes_import_view, name='import_notes'),
    re_path(r'^absencesform/(?P<activite_pk>\d+)/(?P<groupe_pk>\d+)/$',views.absencesform, name='absencesform'),
    re_path(r'^programme_list/$',views.ProgrammeListView.as_view(), name='programme_list'),
    re_path(r'^programme_design/$',views.ProgrammeDesignView.as_view(), name='programme_design'),
    re_path(r'^programme_create/$',views.ProgrammeCreateView.as_view(), name='programme_create'),
    re_path(r'^programme_detail/(?P<pk>\d+)/$',views.ProgrammeDetailView.as_view(), name='programme_detail'),
    re_path(r'^programme_update/(?P<pk>\d+)/$',views.ProgrammeUpdateView.as_view(), name='programme_update'),
    re_path(r'^diplome_create/$',views.DiplomeCreateView.as_view(), name='diplome_create'),
    re_path(r'^diplome_update/(?P<pk>\d+)/$',views.DiplomeUpdateView.as_view(), name='diplome_update'),
    re_path(r'^diplome_delete/(?P<pk>\d+)/$',views.DiplomeDeleteView.as_view(), name='diplome_delete'),
    re_path(r'^specialite_create/$',views.SpecialiteCreateView.as_view(), name='specialite_create'),
    re_path(r'^specialite_update/(?P<pk>\w+)/$',views.SpecialiteUpdateView.as_view(), name='specialite_update'),
    re_path(r'^periode_create/$',views.PeriodeCreateView.as_view(), name='periode_create'),
    re_path(r'^periode_update/(?P<pk>\w+)/$',views.PeriodeUpdateView.as_view(), name='periode_update'),
    re_path(r'^periode_delete/(?P<pk>\d+)/(?P<programme_pk>\d+)/$',views.PeriodeDeleteView.as_view(), name='periode_delete'),
    re_path(r'^periode_programme_create/(?P<programme_pk>\d+)/$',views.PeriodeProgrammeCreateView.as_view(), name='periode_programme_create'),
    re_path(r'^periode_programme_update/(?P<programme_pk>\d+)/(?P<pk>\d+)/$',views.PeriodeProgrammeUpdateView.as_view(), name='periode_programme_update'),
    re_path(r'^periode_programme_delete/(?P<programme_pk>\d+)/(?P<pk>\d+)/$',views.PeriodeProgrammeDeleteView.as_view(), name='periode_programme_delete'),
    re_path(r'^ue_create/(?P<periode_pk>\d+)/(?P<programme_pk>\d+)/$',views.UECreateView.as_view(), name='ue_create'),
    re_path(r'^ue_update/(?P<pk>\d+)/(?P<periode_pk>\d+)/(?P<programme_pk>\d+)/$',views.UEUpdateView.as_view(), name='ue_update'),
    re_path(r'^ue_delete/(?P<pk>\d+)/(?P<programme_pk>\d+)/$',views.UEDeleteView.as_view(), name='ue_delete'),
    re_path(r'^resultat_ue_delete/(?P<pk>\d+)/(?P<inscription_pk>\d+)/$',views.ResultatUEDeleteView.as_view(), name='resultat_ue_delete'),
    re_path(r'^matiere_detail/(?P<pk>\d+)/$',views.MatiereDetailView.as_view(), name='matiere_detail'),
    re_path(r'^matiere_detail_pdf/(?P<pk>\d+)/$',views.MatiereDetailPDFView.as_view(), name='matiere_detail_pdf'),
    re_path(r'^matiere_detail_list_pdf/(?P<programme_pk>\d+)/$',views.MatiereDetailListPDFView.as_view(), name='matiere_detail_list_pdf'),
    re_path(r'^matiere_update/(?P<pk>\d+)/$',views.MatiereUpdateView.as_view(), name='matiere_update'),
    re_path(r'^matiere_competence_update/(?P<matiere_pk>\d+)/$',views.matiere_competence_update_view, name='matiere_competence_update'),
    re_path(r'^matiere_competence_element_update/(?P<pk>\d+)/(?P<matiere_pk>\d+)/$',views.MatiereCompetenceElementUpdateView.as_view(), name='matiere_competence_element_update'),
    re_path(r'^matiere_competence_element_delete/(?P<pk>\d+)/(?P<matiere_pk>\d+)/$',views.MatiereCompetenceElementDeleteView.as_view(), name='matiere_competence_element_delete'),
    re_path(r'^matiere_create/$',views.MatiereCreateView.as_view(), name='matiere_create'),
    re_path(r'^note_list/(?P<matiere_pk>\d+)/(?P<groupe_pk>\d+)/$',views.NoteListView.as_view(), name='note_list'),
    re_path(r'^note_update/(?P<groupe_pk>\d+)/(?P<matiere_pk>\d+)/$',views.note_update, name='note_update'),
    re_path(r'^note_pfe_update/(?P<groupe_pk>\d+)/(?P<module_pk>\d+)/$',views.note_pfe_update, name='note_pfe_update'),
    re_path(r'^export_fiche_eval_pfe/(?P<groupe_pk>\d+)/(?P<module_pk>\d+)/$',views.export_fiche_eval_pfe, name='export_fiche_eval_pfe'),
    re_path(r'^note_pfe_lock/(?P<groupe_pk>\d+)/(?P<module_pk>\d+)/$',views.note_pfe_lock, name='note_pfe_lock'),
    path('notes_formation_list', views.NotesFormationListView.as_view(), name='notes_formation_list'),
    path('notes_formation_pfe_list', views.NotesFormationPFEListView.as_view(), name='notes_formation_pfe_list'),
    re_path(r'^notes_formation_detail/(?P<formation_pk>\d+)/(?P<periode_pk>\d+)/$',views.NotesFormationDetailView.as_view(), name='notes_formation_detail'),
    re_path(r'^notes_formation_coordinateur_detail/(?P<formation_pk>\d+)/(?P<periode_pk>\d+)/(?P<module_pk>\d+)/$',views.NotesFormationCoordinateurDetailView.as_view(), name='notes_formation_coordinateur_detail'),
    path('tutorat_list', views.TutoratListView.as_view(), name='tutorat_list'),
    path('tutorats_import', views.tutorat_import_view, name='tutorats_import'),
    path('coordination', views.CoordinationModuleListView.as_view(), name='coordination'),
    path('coordination_notes', views.CoordinationNotesModuleListView.as_view(), name='coordination_notes'),
    re_path(r'^module_detail/(?P<pk>\d+)/$',views.ModuleDetailView.as_view(), name='module_detail'),
    re_path(r'^module_copy/(?P<module_pk>\d+)/$',views.ModuleCopyView.as_view(), name='module_copy'),
    re_path(r'^module_create/(?P<formation_pk>\d+)/(?P<periode_pk>\d+)/$',views.ModuleCreateView.as_view(), name='module_create'),
    re_path(r'^evaluation_create/(?P<module_pk>\d+)/$',views.EvaluationCreateView.as_view(), name='evaluation_create'),
    re_path(r'^evaluation_update/(?P<pk>\d+)/(?P<module_pk>\d+)/$',views.EvaluationUpdateView.as_view(), name='evaluation_update'),
    re_path(r'^evaluation_delete/(?P<pk>\d+)/(?P<module_pk>\d+)/$',views.EvaluationDeleteView.as_view(), name='evaluation_delete'),
    re_path(r'^evaluation_competence_update/(?P<evaluation_pk>\d+)/$',views.evaluation_competence_update_view, name='evaluation_competence_update'),
    re_path(r'^evaluation_competence_element_update/(?P<pk>\d+)/(?P<evaluation_pk>\d+)/$',views.EvaluationCompetenceElementUpdateView.as_view(), name='evaluation_competence_element_update'),
    re_path(r'^evaluation_competence_element_delete/(?P<pk>\d+)/(?P<evaluation_pk>\d+)/$',views.EvaluationCompetenceElementDeleteView.as_view(), name='evaluation_competence_element_delete'),
    re_path(r'^semainier_create/(?P<module_pk>\d+)/$',views.SemainierCreateView.as_view(), name='semainier_create'),
    re_path(r'^semainier_update/(?P<pk>\d+)/(?P<module_pk>\d+)/$',views.SemainierUpdateView.as_view(), name='semainier_update'),
    re_path(r'^semainier_delete/(?P<pk>\d+)/(?P<module_pk>\d+)/$',views.SemainierDeleteView.as_view(), name='semainier_delete'),
    path('charge_list', views.charge_list_view, name='charge_list'),
    path('charge_batch_create', views.charge_batch_create_view, name='charge_batch_create'),
    re_path(r'^charge_enseignant/(?P<enseignant_pk>\d+)/$', views.ChargeEnseignantView.as_view(), name='charge_enseignant'),
    re_path(r'^charge_enseignant_detail/(?P<enseignant_pk>\d+)/$', views.ChargeEnseignantDetailView.as_view(), name='charge_enseignant_detail'),    
    re_path(r'^charge_enseignant_create/(?P<enseignant_pk>\d+)/$', views.ChargeEnseignantCreateView.as_view(), name='charge_enseignant_create'),
    re_path(r'^charge_enseignant_update/(?P<pk>\d+)/$', views.ChargeEnseignantUpdateView.as_view(), name='charge_enseignant_update'),
    re_path(r'^charge_enseignant_delete/(?P<enseignant_pk>\d+)/(?P<pk>\d+)/$', views.ChargeEnseignantDeleteView.as_view(), name='charge_enseignant_delete'),
    path('activite_charge_config_list', views.ActiviteChargeConfigListView.as_view(), name='activite_charge_config_list'),
    path('activite_charge_config_create', views.ActiviteChargeConfigCreateView.as_view(), name='activite_charge_config_create'),
    re_path(r'^activite_charge_config_update/(?P<pk>\d+)/$', views.ActiviteChargeConfigUpdateView.as_view(), name='activite_charge_config_update'),
    re_path(r'^activite_charge_config_delete/(?P<pk>\d+)/$', views.ActiviteChargeConfigDeleteView.as_view(), name='activite_charge_config_delete'),
    re_path(r'^charge_selon_config_create/(?P<enseignant_pk>\d+)/$', views.charge_selon_config_create_view, name='charge_selon_config_create'),
    path('enseignant_list', views.EnseignantListView.as_view(), name='enseignant_list'),
    path('enseignant_import', views.enseignants_import_view, name='enseignant_import'),
    path('enseignant_create', views.EnseignantCreateView.as_view(), name='enseignant_create'),
    re_path(r'^enseignant_module_absences/(?P<enseignant_pk>\d+)/(?P<module_pk>\d+)/$',views.AbsenceEnseignantView.as_view(), name='enseignant_module_absences'),
    re_path(r'^enseignant_edt/(?P<enseignant_pk>\d+)/$',views.EnseignantEDTView.as_view(), name='enseignant_edt'),
    path('enseignant_groupe_all_list', views.EnseignantGroupeAllListView.as_view(), name='enseignant_groupe_all_list'),
    re_path(r'^enseignant_update/(?P<pk>\d+)/$',views.EnseignantUpdateView.as_view(), name='enseignant_update'),
    re_path(r'^enseignant_detail/(?P<pk>\d+)/$',views.EnseignantDetailView.as_view(), name='enseignant_detail'),
    path('signaler_absence_enseignant', views.signaler_absence_enseignant, name='signaler_absence_enseignant'),
    
    re_path(r'^export_notes/(?P<groupe_pk>\d+)/(?P<module_pk>\d+)/$',views.export_notes, name='export_notes'),
    re_path(r'^notes_module_import/(?P<module_pk>\d+)/(?P<groupe_pk>\d+)/$',views.notes_module_import_view, name='notes_module_import'),
    re_path(r'^export_inscriptions/(?P<formation_pk>\d+)/$',views.export_inscriptions, name='export_inscriptions'),
    re_path(r'^import_affectation_groupe/$',views.affectation_groupe_view, name='import_affectation_groupe'),
    re_path(r'^import_affectation_pfe/$',views.affectation_pfe_view, name='import_affectation_pfe'),
    re_path(r'^import_affectation_pfe_valide/$',views.affectation_pfe_valide_view, name='import_affectation_pfe_valide'),
    re_path(r'^settings_update_view/(?P<pk>\d+)/$', views.SettingsUpdateView.as_view(), name='settings_update_view'),
    path('settings', views.SettingsDetailView.as_view(), name='settings'),
    path('pays_import', views.pays_import_view, name='pays_import'),
    path('wilayas_import', views.wilayas_import_view, name='wilayas_import'),
    path('communes_import', views.communes_import_view, name='communes_import'),
    path('residenceuniv_list', views.ResidenceUnivListView.as_view(), name='residenceuniv_list'),
    path('residenceuniv_create', views.ResidenceUnivCreateView.as_view(), name='residenceuniv_create'),

################################################# URLS Reget

    path('ChapitreCreate', views.ChapitreCreate, name='ChapitreCreate'),
    path('ChapitreShow', views.ChapitreShow, name='ChapitreShow'),
    path('ChapitreDelete/<int:id>/', views.ChapitreDelete, name='ChapitreDelete'),

    path('ArticleCreate/<int:art>/', views.ArticleCreate, name="ArticleCreate"),
    path('ArticleDelete/<int:art>/', views.ArticleDelete, name="ArticleDelete"),

    path('CreditCreate/', views.CreditCreate, name="CreditCreate"),
    path('CreditAssociate/<int:art>/', views.CreditAssociate, name="CreditAssociate"),
    path('CreditDelete/<int:art>/', views.CreditDelete, name="CreditDelete"),
   
    path('aa_pdf', views.aa_PDFView.as_view(), name='aa_pdf'),
    path('BordereauCreate/<int:crdt>/', views.BordereauCreate, name="BordereauCreate"),
    path('LitImput', views.LitImput, name='LitImput'),
    path('PieceCreate/<int:brdr>/', views.PieceCreate, name='PieceCreate'),
    path('PieceDelete/<int:pc>/', views.PieceDelete, name="PieceDelete"),
    path('aa_bordereau_pdf/<bordereau_pk>/', views.aa_bordereau_PDFView.as_view(), name='aa_bordereau_pdf'),

    




]