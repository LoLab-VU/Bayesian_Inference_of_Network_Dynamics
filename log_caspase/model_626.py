# exported from PySB model 'model'

from pysb import Model, Monomer, Parameter, Expression, Compartment, Rule, Observable, Initial, MatchOnce, Annotation, ANY, WILD

Model()

Monomer('C6A', ['C8pro'])
Monomer('Ligand', ['Receptor'])
Monomer('ParpU', ['C3A'])
Monomer('C3ub')
Monomer('C3A', ['Xiap', 'ParpU', 'C6pro'])
Monomer('Xiap', ['C3A'])
Monomer('C8A', ['C3pro'])
Monomer('C3pro', ['C8A'])
Monomer('Receptor', ['Ligand', 'Fadd'])
Monomer('C6pro', ['C3A'])
Monomer('Fadd', ['Receptor', 'C8pro'])
Monomer('C8pro', ['Fadd', 'C6A'])
Monomer('ParpC')

Parameter('bind_0_Ligand_binder_Receptor_binder_target_2kf', 1.0)
Parameter('bind_0_Ligand_binder_Receptor_binder_target_1kr', 1.0)
Parameter('bind_0_Receptor_binder_Fadd_binder_target_2kf', 1.0)
Parameter('bind_0_Receptor_binder_Fadd_binder_target_1kr', 1.0)
Parameter('substrate_binding_0_Fadd_catalyzer_C8pro_substrate_2kf', 1.0)
Parameter('substrate_binding_0_Fadd_catalyzer_C8pro_substrate_1kr', 1.0)
Parameter('catalytic_step_0_Fadd_catalyzer_C8pro_substrate_C8A_product_1kc', 1.0)
Parameter('catalysis_0_C8A_catalyzer_C3pro_substrate_C3A_product_2kf', 1.0)
Parameter('catalysis_0_C8A_catalyzer_C3pro_substrate_C3A_product_1kr', 1.0)
Parameter('catalysis_1_C8A_catalyzer_C3pro_substrate_C3A_product_1kc', 1.0)
Parameter('catalysis_0_Xiap_catalyzer_C3A_substrate_C3ub_product_2kf', 1.0)
Parameter('catalysis_0_Xiap_catalyzer_C3A_substrate_C3ub_product_1kr', 1.0)
Parameter('catalysis_1_Xiap_catalyzer_C3A_substrate_C3ub_product_1kc', 1.0)
Parameter('catalysis_0_C3A_catalyzer_ParpU_substrate_ParpC_product_2kf', 1.0)
Parameter('catalysis_0_C3A_catalyzer_ParpU_substrate_ParpC_product_1kr', 1.0)
Parameter('catalysis_1_C3A_catalyzer_ParpU_substrate_ParpC_product_1kc', 1.0)
Parameter('catalysis_0_C3A_catalyzer_C6pro_substrate_C6A_product_2kf', 1.0)
Parameter('catalysis_0_C3A_catalyzer_C6pro_substrate_C6A_product_1kr', 1.0)
Parameter('catalysis_1_C3A_catalyzer_C6pro_substrate_C6A_product_1kc', 1.0)
Parameter('catalysis_0_C6A_catalyzer_C8pro_substrate_C8A_product_2kf', 1.0)
Parameter('catalysis_0_C6A_catalyzer_C8pro_substrate_C8A_product_1kr', 1.0)
Parameter('catalysis_1_C6A_catalyzer_C8pro_substrate_C8A_product_1kc', 1.0)
Parameter('C6A_0', 0.0)
Parameter('Ligand_0', 1000.0)
Parameter('ParpU_0', 1000000.0)
Parameter('C3ub_0', 0.0)
Parameter('C3A_0', 0.0)
Parameter('Xiap_0', 156500.0)
Parameter('C8A_0', 0.0)
Parameter('C3pro_0', 21000.0)
Parameter('Receptor_0', 100.0)
Parameter('C6pro_0', 100.0)
Parameter('Fadd_0', 130000.0)
Parameter('C8pro_0', 130000.0)
Parameter('ParpC_0', 0.0)

Observable('C6A_obs', C6A())
Observable('Ligand_obs', Ligand())
Observable('ParpU_obs', ParpU())
Observable('C3ub_obs', C3ub())
Observable('C3A_obs', C3A())
Observable('Xiap_obs', Xiap())
Observable('C8A_obs', C8A())
Observable('C3pro_obs', C3pro())
Observable('Receptor_obs', Receptor())
Observable('C6pro_obs', C6pro())
Observable('Fadd_obs', Fadd())
Observable('C8pro_obs', C8pro())
Observable('ParpC_obs', ParpC())

Rule('bind_0_Ligand_binder_Receptor_binder_target', Ligand(Receptor=None) + Receptor(Ligand=None, Fadd=None) | Ligand(Receptor=1) % Receptor(Ligand=1, Fadd=None), bind_0_Ligand_binder_Receptor_binder_target_2kf, bind_0_Ligand_binder_Receptor_binder_target_1kr)
Rule('bind_0_Receptor_binder_Fadd_binder_target', Receptor(Ligand=ANY, Fadd=None) + Fadd(Receptor=None, C8pro=None) | Receptor(Ligand=ANY, Fadd=1) % Fadd(Receptor=1, C8pro=None), bind_0_Receptor_binder_Fadd_binder_target_2kf, bind_0_Receptor_binder_Fadd_binder_target_1kr)
Rule('substrate_binding_0_Fadd_catalyzer_C8pro_substrate', Fadd(Receptor=ANY, C8pro=None) + C8pro(Fadd=None, C6A=None) | Fadd(Receptor=ANY, C8pro=1) % C8pro(Fadd=1, C6A=None), substrate_binding_0_Fadd_catalyzer_C8pro_substrate_2kf, substrate_binding_0_Fadd_catalyzer_C8pro_substrate_1kr)
Rule('catalytic_step_0_Fadd_catalyzer_C8pro_substrate_C8A_product', Fadd(Receptor=ANY, C8pro=1) % C8pro(Fadd=1, C6A=None) >> Fadd(Receptor=ANY, C8pro=None) + C8A(C3pro=None), catalytic_step_0_Fadd_catalyzer_C8pro_substrate_C8A_product_1kc)
Rule('catalysis_0_C8A_catalyzer_C3pro_substrate_C3A_product', C8A(C3pro=None) + C3pro(C8A=None) | C8A(C3pro=1) % C3pro(C8A=1), catalysis_0_C8A_catalyzer_C3pro_substrate_C3A_product_2kf, catalysis_0_C8A_catalyzer_C3pro_substrate_C3A_product_1kr)
Rule('catalysis_1_C8A_catalyzer_C3pro_substrate_C3A_product', C8A(C3pro=1) % C3pro(C8A=1) >> C8A(C3pro=None) + C3A(Xiap=None, ParpU=None, C6pro=None), catalysis_1_C8A_catalyzer_C3pro_substrate_C3A_product_1kc)
Rule('catalysis_0_Xiap_catalyzer_C3A_substrate_C3ub_product', Xiap(C3A=None) + C3A(Xiap=None, ParpU=None, C6pro=None) | Xiap(C3A=1) % C3A(Xiap=1, ParpU=None, C6pro=None), catalysis_0_Xiap_catalyzer_C3A_substrate_C3ub_product_2kf, catalysis_0_Xiap_catalyzer_C3A_substrate_C3ub_product_1kr)
Rule('catalysis_1_Xiap_catalyzer_C3A_substrate_C3ub_product', Xiap(C3A=1) % C3A(Xiap=1, ParpU=None, C6pro=None) >> Xiap(C3A=None) + C3ub(), catalysis_1_Xiap_catalyzer_C3A_substrate_C3ub_product_1kc)
Rule('catalysis_0_C3A_catalyzer_ParpU_substrate_ParpC_product', C3A(Xiap=None, ParpU=None, C6pro=None) + ParpU(C3A=None) | C3A(Xiap=None, ParpU=1, C6pro=None) % ParpU(C3A=1), catalysis_0_C3A_catalyzer_ParpU_substrate_ParpC_product_2kf, catalysis_0_C3A_catalyzer_ParpU_substrate_ParpC_product_1kr)
Rule('catalysis_1_C3A_catalyzer_ParpU_substrate_ParpC_product', C3A(Xiap=None, ParpU=1, C6pro=None) % ParpU(C3A=1) >> C3A(Xiap=None, ParpU=None, C6pro=None) + ParpC(), catalysis_1_C3A_catalyzer_ParpU_substrate_ParpC_product_1kc)
Rule('catalysis_0_C3A_catalyzer_C6pro_substrate_C6A_product', C3A(Xiap=None, ParpU=None, C6pro=None) + C6pro(C3A=None) | C3A(Xiap=None, ParpU=None, C6pro=1) % C6pro(C3A=1), catalysis_0_C3A_catalyzer_C6pro_substrate_C6A_product_2kf, catalysis_0_C3A_catalyzer_C6pro_substrate_C6A_product_1kr)
Rule('catalysis_1_C3A_catalyzer_C6pro_substrate_C6A_product', C3A(Xiap=None, ParpU=None, C6pro=1) % C6pro(C3A=1) >> C3A(Xiap=None, ParpU=None, C6pro=None) + C6A(C8pro=None), catalysis_1_C3A_catalyzer_C6pro_substrate_C6A_product_1kc)
Rule('catalysis_0_C6A_catalyzer_C8pro_substrate_C8A_product', C6A(C8pro=None) + C8pro(Fadd=None, C6A=None) | C6A(C8pro=1) % C8pro(Fadd=None, C6A=1), catalysis_0_C6A_catalyzer_C8pro_substrate_C8A_product_2kf, catalysis_0_C6A_catalyzer_C8pro_substrate_C8A_product_1kr)
Rule('catalysis_1_C6A_catalyzer_C8pro_substrate_C8A_product', C6A(C8pro=1) % C8pro(Fadd=None, C6A=1) >> C6A(C8pro=None) + C8A(C3pro=None), catalysis_1_C6A_catalyzer_C8pro_substrate_C8A_product_1kc)

Initial(C6A(C8pro=None), C6A_0)
Initial(Ligand(Receptor=None), Ligand_0)
Initial(ParpU(C3A=None), ParpU_0)
Initial(C3ub(), C3ub_0)
Initial(C3A(Xiap=None, ParpU=None, C6pro=None), C3A_0)
Initial(Xiap(C3A=None), Xiap_0)
Initial(C8A(C3pro=None), C8A_0)
Initial(C3pro(C8A=None), C3pro_0)
Initial(Receptor(Ligand=None, Fadd=None), Receptor_0)
Initial(C6pro(C3A=None), C6pro_0)
Initial(Fadd(Receptor=None, C8pro=None), Fadd_0)
Initial(C8pro(Fadd=None, C6A=None), C8pro_0)
Initial(ParpC(), ParpC_0)

