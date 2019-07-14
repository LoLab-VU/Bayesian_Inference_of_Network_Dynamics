# exported from PySB model 'model'

from pysb import Model, Monomer, Parameter, Expression, Compartment, Rule, Observable, Initial, MatchOnce, Annotation, ANY, WILD

Model()

Monomer('C6A', ['C8pro'])
Monomer('BaxA', ['BaxM', 'BaxA_1', 'BaxA_2', 'SmacM'])
Monomer('Ligand', ['Receptor'])
Monomer('C6pro', ['C3A'])
Monomer('ParpU', ['C3A'])
Monomer('BidU', ['C8A'])
Monomer('BidT')
Monomer('C3A', ['Xiap', 'ParpU', 'C6pro'])
Monomer('BidM', ['BaxM'])
Monomer('BaxM', ['BidM', 'BaxA'])
Monomer('C8A', ['BidU', 'C3pro'])
Monomer('Xiap', ['SmacC', 'C3A'])
Monomer('Receptor', ['Ligand', 'Fadd'])
Monomer('C3ub')
Monomer('Fadd', ['Receptor', 'C8pro'])
Monomer('C3pro', ['C8A'])
Monomer('SmacM', ['BaxA'])
Monomer('SmacC', ['Xiap'])
Monomer('C8pro', ['Fadd', 'C6A'])
Monomer('ParpC')

Parameter('bind_0_Ligand_binder_Receptor_binder_target_2kf', 1.0)
Parameter('bind_0_Ligand_binder_Receptor_binder_target_1kr', 1.0)
Parameter('bind_0_Receptor_binder_Fadd_binder_target_2kf', 1.0)
Parameter('bind_0_Receptor_binder_Fadd_binder_target_1kr', 1.0)
Parameter('substrate_binding_0_Fadd_catalyzer_C8pro_substrate_2kf', 1.0)
Parameter('substrate_binding_0_Fadd_catalyzer_C8pro_substrate_1kr', 1.0)
Parameter('catalytic_step_0_Fadd_catalyzer_C8pro_substrate_C8A_product_1kc', 1.0)
Parameter('catalysis_0_C8A_catalyzer_BidU_substrate_BidT_product_2kf', 1.0)
Parameter('catalysis_0_C8A_catalyzer_BidU_substrate_BidT_product_1kr', 1.0)
Parameter('catalysis_1_C8A_catalyzer_BidU_substrate_BidT_product_1kc', 1.0)
Parameter('inhibition_0_SmacC_inhibitor_Xiap_inh_target_2kf', 1.0)
Parameter('inhibition_0_SmacC_inhibitor_Xiap_inh_target_1kr', 1.0)
Parameter('catalysis_0_Xiap_catalyzer_C3A_substrate_C3ub_product_2kf', 1.0)
Parameter('catalysis_0_Xiap_catalyzer_C3A_substrate_C3ub_product_1kr', 1.0)
Parameter('catalysis_1_Xiap_catalyzer_C3A_substrate_C3ub_product_1kc', 1.0)
Parameter('catalysis_0_C3A_catalyzer_ParpU_substrate_ParpC_product_2kf', 1.0)
Parameter('catalysis_0_C3A_catalyzer_ParpU_substrate_ParpC_product_1kr', 1.0)
Parameter('catalysis_1_C3A_catalyzer_ParpU_substrate_ParpC_product_1kc', 1.0)
Parameter('equilibration_0_BidT_equil_a_BidM_equil_b_1kf', 1.0)
Parameter('equilibration_0_BidT_equil_a_BidM_equil_b_1kr', 1.0)
Parameter('catalysis_0_BidM_catalyzer_BaxM_substrate_BaxA_product_2kf', 1.0)
Parameter('catalysis_0_BidM_catalyzer_BaxM_substrate_BaxA_product_1kr', 1.0)
Parameter('catalysis_1_BidM_catalyzer_BaxM_substrate_BaxA_product_1kc', 1.0)
Parameter('self_catalyze_0_BaxA_self_catalyzer_BaxM_self_substrate_2kf', 1.0)
Parameter('self_catalyze_0_BaxA_self_catalyzer_BaxM_self_substrate_1kr', 1.0)
Parameter('self_catalyze_1_BaxA_self_catalyzer_BaxM_self_substrate_1kc', 1.0)
Parameter('pore_formation_0_BaxA_pore_2kf', 1.0)
Parameter('pore_formation_0_BaxA_pore_1kr', 1.0)
Parameter('pore_formation_1_BaxA_pore_2kf', 1.0)
Parameter('pore_formation_1_BaxA_pore_1kr', 1.0)
Parameter('pore_formation_2_BaxA_pore_2kf', 1.0)
Parameter('pore_formation_2_BaxA_pore_1kr', 1.0)
Parameter('transport_0_BaxA_pore_SmacM_cargo_M_SmacC_cargo_C_2kf', 1.0)
Parameter('transport_0_BaxA_pore_SmacM_cargo_M_SmacC_cargo_C_1kr', 1.0)
Parameter('transport_1_BaxA_pore_SmacM_cargo_M_SmacC_cargo_C_1kc', 1.0)
Parameter('catalysis_0_C8A_catalyzer_C3pro_substrate_C3A_product_2kf', 1.0)
Parameter('catalysis_0_C8A_catalyzer_C3pro_substrate_C3A_product_1kr', 1.0)
Parameter('catalysis_1_C8A_catalyzer_C3pro_substrate_C3A_product_1kc', 1.0)
Parameter('catalysis_0_C3A_catalyzer_C6pro_substrate_C6A_product_2kf', 1.0)
Parameter('catalysis_0_C3A_catalyzer_C6pro_substrate_C6A_product_1kr', 1.0)
Parameter('catalysis_1_C3A_catalyzer_C6pro_substrate_C6A_product_1kc', 1.0)
Parameter('catalysis_0_C6A_catalyzer_C8pro_substrate_C8A_product_2kf', 1.0)
Parameter('catalysis_0_C6A_catalyzer_C8pro_substrate_C8A_product_1kr', 1.0)
Parameter('catalysis_1_C6A_catalyzer_C8pro_substrate_C8A_product_1kc', 1.0)
Parameter('C6A_0', 0.0)
Parameter('BaxA_0', 0.0)
Parameter('Ligand_0', 1000.0)
Parameter('C6pro_0', 100.0)
Parameter('ParpU_0', 1000000.0)
Parameter('BidU_0', 171000.0)
Parameter('BidT_0', 0.0)
Parameter('C3A_0', 0.0)
Parameter('BidM_0', 0.0)
Parameter('BaxM_0', 40000.0)
Parameter('C8A_0', 0.0)
Parameter('Xiap_0', 71750.0)
Parameter('Receptor_0', 100.0)
Parameter('C3ub_0', 0.0)
Parameter('Fadd_0', 130000.0)
Parameter('C3pro_0', 21000.0)
Parameter('SmacM_0', 100000.0)
Parameter('SmacC_0', 0.0)
Parameter('C8pro_0', 130000.0)
Parameter('ParpC_0', 0.0)

Observable('C6A_obs', C6A())
Observable('BaxA_obs', BaxA())
Observable('Ligand_obs', Ligand())
Observable('C6pro_obs', C6pro())
Observable('ParpU_obs', ParpU())
Observable('BidU_obs', BidU())
Observable('BidT_obs', BidT())
Observable('C3A_obs', C3A())
Observable('BidM_obs', BidM())
Observable('BaxM_obs', BaxM())
Observable('C8A_obs', C8A())
Observable('Xiap_obs', Xiap())
Observable('Receptor_obs', Receptor())
Observable('C3ub_obs', C3ub())
Observable('Fadd_obs', Fadd())
Observable('C3pro_obs', C3pro())
Observable('SmacM_obs', SmacM())
Observable('SmacC_obs', SmacC())
Observable('C8pro_obs', C8pro())
Observable('ParpC_obs', ParpC())

Rule('bind_0_Ligand_binder_Receptor_binder_target', Ligand(Receptor=None) + Receptor(Ligand=None, Fadd=None) | Ligand(Receptor=1) % Receptor(Ligand=1, Fadd=None), bind_0_Ligand_binder_Receptor_binder_target_2kf, bind_0_Ligand_binder_Receptor_binder_target_1kr)
Rule('bind_0_Receptor_binder_Fadd_binder_target', Receptor(Ligand=ANY, Fadd=None) + Fadd(Receptor=None, C8pro=None) | Receptor(Ligand=ANY, Fadd=1) % Fadd(Receptor=1, C8pro=None), bind_0_Receptor_binder_Fadd_binder_target_2kf, bind_0_Receptor_binder_Fadd_binder_target_1kr)
Rule('substrate_binding_0_Fadd_catalyzer_C8pro_substrate', Fadd(Receptor=ANY, C8pro=None) + C8pro(Fadd=None, C6A=None) | Fadd(Receptor=ANY, C8pro=1) % C8pro(Fadd=1, C6A=None), substrate_binding_0_Fadd_catalyzer_C8pro_substrate_2kf, substrate_binding_0_Fadd_catalyzer_C8pro_substrate_1kr)
Rule('catalytic_step_0_Fadd_catalyzer_C8pro_substrate_C8A_product', Fadd(Receptor=ANY, C8pro=1) % C8pro(Fadd=1, C6A=None) >> Fadd(Receptor=ANY, C8pro=None) + C8A(BidU=None, C3pro=None), catalytic_step_0_Fadd_catalyzer_C8pro_substrate_C8A_product_1kc)
Rule('catalysis_0_C8A_catalyzer_BidU_substrate_BidT_product', C8A(BidU=None, C3pro=None) + BidU(C8A=None) | C8A(BidU=1, C3pro=None) % BidU(C8A=1), catalysis_0_C8A_catalyzer_BidU_substrate_BidT_product_2kf, catalysis_0_C8A_catalyzer_BidU_substrate_BidT_product_1kr)
Rule('catalysis_1_C8A_catalyzer_BidU_substrate_BidT_product', C8A(BidU=1, C3pro=None) % BidU(C8A=1) >> C8A(BidU=None, C3pro=None) + BidT(), catalysis_1_C8A_catalyzer_BidU_substrate_BidT_product_1kc)
Rule('inhibition_0_SmacC_inhibitor_Xiap_inh_target', SmacC(Xiap=None) + Xiap(SmacC=None, C3A=None) | SmacC(Xiap=1) % Xiap(SmacC=1, C3A=None), inhibition_0_SmacC_inhibitor_Xiap_inh_target_2kf, inhibition_0_SmacC_inhibitor_Xiap_inh_target_1kr)
Rule('catalysis_0_Xiap_catalyzer_C3A_substrate_C3ub_product', Xiap(SmacC=None, C3A=None) + C3A(Xiap=None, ParpU=None, C6pro=None) | Xiap(SmacC=None, C3A=1) % C3A(Xiap=1, ParpU=None, C6pro=None), catalysis_0_Xiap_catalyzer_C3A_substrate_C3ub_product_2kf, catalysis_0_Xiap_catalyzer_C3A_substrate_C3ub_product_1kr)
Rule('catalysis_1_Xiap_catalyzer_C3A_substrate_C3ub_product', Xiap(SmacC=None, C3A=1) % C3A(Xiap=1, ParpU=None, C6pro=None) >> Xiap(SmacC=None, C3A=None) + C3ub(), catalysis_1_Xiap_catalyzer_C3A_substrate_C3ub_product_1kc)
Rule('catalysis_0_C3A_catalyzer_ParpU_substrate_ParpC_product', C3A(Xiap=None, ParpU=None, C6pro=None) + ParpU(C3A=None) | C3A(Xiap=None, ParpU=1, C6pro=None) % ParpU(C3A=1), catalysis_0_C3A_catalyzer_ParpU_substrate_ParpC_product_2kf, catalysis_0_C3A_catalyzer_ParpU_substrate_ParpC_product_1kr)
Rule('catalysis_1_C3A_catalyzer_ParpU_substrate_ParpC_product', C3A(Xiap=None, ParpU=1, C6pro=None) % ParpU(C3A=1) >> C3A(Xiap=None, ParpU=None, C6pro=None) + ParpC(), catalysis_1_C3A_catalyzer_ParpU_substrate_ParpC_product_1kc)
Rule('equilibration_0_BidT_equil_a_BidM_equil_b', BidT() | BidM(BaxM=None), equilibration_0_BidT_equil_a_BidM_equil_b_1kf, equilibration_0_BidT_equil_a_BidM_equil_b_1kr)
Rule('catalysis_0_BidM_catalyzer_BaxM_substrate_BaxA_product', BidM(BaxM=None) + BaxM(BidM=None, BaxA=None) | BidM(BaxM=1) % BaxM(BidM=1, BaxA=None), catalysis_0_BidM_catalyzer_BaxM_substrate_BaxA_product_2kf, catalysis_0_BidM_catalyzer_BaxM_substrate_BaxA_product_1kr)
Rule('catalysis_1_BidM_catalyzer_BaxM_substrate_BaxA_product', BidM(BaxM=1) % BaxM(BidM=1, BaxA=None) >> BidM(BaxM=None) + BaxA(BaxM=None, BaxA_1=None, BaxA_2=None, SmacM=None), catalysis_1_BidM_catalyzer_BaxM_substrate_BaxA_product_1kc)
Rule('self_catalyze_0_BaxA_self_catalyzer_BaxM_self_substrate', BaxA(BaxM=None, BaxA_1=None, BaxA_2=None, SmacM=None) + BaxM(BidM=None, BaxA=None) | BaxA(BaxM=1, BaxA_1=None, BaxA_2=None, SmacM=None) % BaxM(BidM=None, BaxA=1), self_catalyze_0_BaxA_self_catalyzer_BaxM_self_substrate_2kf, self_catalyze_0_BaxA_self_catalyzer_BaxM_self_substrate_1kr)
Rule('self_catalyze_1_BaxA_self_catalyzer_BaxM_self_substrate', BaxA(BaxM=1, BaxA_1=None, BaxA_2=None, SmacM=None) % BaxM(BidM=None, BaxA=1) >> BaxA(BaxM=None, BaxA_1=None, BaxA_2=None, SmacM=None) + BaxA(BaxM=None, BaxA_1=None, BaxA_2=None, SmacM=None), self_catalyze_1_BaxA_self_catalyzer_BaxM_self_substrate_1kc)
Rule('pore_formation_0_BaxA_pore', BaxA(BaxM=None, BaxA_1=None, BaxA_2=None, SmacM=None) + BaxA(BaxM=None, BaxA_1=None, BaxA_2=None, SmacM=None) | BaxA(BaxM=None, BaxA_1=None, BaxA_2=1, SmacM=None) % BaxA(BaxM=None, BaxA_1=1, BaxA_2=None, SmacM=None), pore_formation_0_BaxA_pore_2kf, pore_formation_0_BaxA_pore_1kr)
Rule('pore_formation_1_BaxA_pore', BaxA(BaxM=None, BaxA_1=None, BaxA_2=None, SmacM=None) + BaxA(BaxM=None, BaxA_1=None, BaxA_2=1, SmacM=None) % BaxA(BaxM=None, BaxA_1=1, BaxA_2=None, SmacM=None) | BaxA(BaxM=None, BaxA_1=3, BaxA_2=1, SmacM=None) % BaxA(BaxM=None, BaxA_1=1, BaxA_2=2, SmacM=None) % BaxA(BaxM=None, BaxA_1=2, BaxA_2=3, SmacM=None), pore_formation_1_BaxA_pore_2kf, pore_formation_1_BaxA_pore_1kr)
Rule('pore_formation_2_BaxA_pore', BaxA(BaxM=None, BaxA_1=None, BaxA_2=None, SmacM=None) + BaxA(BaxM=None, BaxA_1=3, BaxA_2=1, SmacM=None) % BaxA(BaxM=None, BaxA_1=1, BaxA_2=2, SmacM=None) % BaxA(BaxM=None, BaxA_1=2, BaxA_2=3, SmacM=None) | BaxA(BaxM=None, BaxA_1=4, BaxA_2=1, SmacM=None) % BaxA(BaxM=None, BaxA_1=1, BaxA_2=2, SmacM=None) % BaxA(BaxM=None, BaxA_1=2, BaxA_2=3, SmacM=None) % BaxA(BaxM=None, BaxA_1=3, BaxA_2=4, SmacM=None), pore_formation_2_BaxA_pore_2kf, pore_formation_2_BaxA_pore_1kr)
Rule('transport_0_BaxA_pore_SmacM_cargo_M_SmacC_cargo_C', BaxA(BaxM=None, BaxA_1=4, BaxA_2=1, SmacM=None) % BaxA(BaxM=None, BaxA_1=1, BaxA_2=2, SmacM=None) % BaxA(BaxM=None, BaxA_1=2, BaxA_2=3, SmacM=None) % BaxA(BaxM=None, BaxA_1=3, BaxA_2=4, SmacM=None) + SmacM(BaxA=None) | BaxA(BaxM=None, BaxA_1=4, BaxA_2=1, SmacM=None) % BaxA(BaxM=None, BaxA_1=1, BaxA_2=2, SmacM=None) % BaxA(BaxM=None, BaxA_1=2, BaxA_2=3, SmacM=None) % BaxA(BaxM=None, BaxA_1=3, BaxA_2=4, SmacM=5) % SmacM(BaxA=5), transport_0_BaxA_pore_SmacM_cargo_M_SmacC_cargo_C_2kf, transport_0_BaxA_pore_SmacM_cargo_M_SmacC_cargo_C_1kr)
Rule('transport_1_BaxA_pore_SmacM_cargo_M_SmacC_cargo_C', BaxA(BaxM=None, BaxA_1=4, BaxA_2=1, SmacM=None) % BaxA(BaxM=None, BaxA_1=1, BaxA_2=2, SmacM=None) % BaxA(BaxM=None, BaxA_1=2, BaxA_2=3, SmacM=None) % BaxA(BaxM=None, BaxA_1=3, BaxA_2=4, SmacM=5) % SmacM(BaxA=5) >> BaxA(BaxM=None, BaxA_1=4, BaxA_2=1, SmacM=None) % BaxA(BaxM=None, BaxA_1=1, BaxA_2=2, SmacM=None) % BaxA(BaxM=None, BaxA_1=2, BaxA_2=3, SmacM=None) % BaxA(BaxM=None, BaxA_1=3, BaxA_2=4, SmacM=None) + SmacC(Xiap=None), transport_1_BaxA_pore_SmacM_cargo_M_SmacC_cargo_C_1kc)
Rule('catalysis_0_C8A_catalyzer_C3pro_substrate_C3A_product', C8A(BidU=None, C3pro=None) + C3pro(C8A=None) | C8A(BidU=None, C3pro=1) % C3pro(C8A=1), catalysis_0_C8A_catalyzer_C3pro_substrate_C3A_product_2kf, catalysis_0_C8A_catalyzer_C3pro_substrate_C3A_product_1kr)
Rule('catalysis_1_C8A_catalyzer_C3pro_substrate_C3A_product', C8A(BidU=None, C3pro=1) % C3pro(C8A=1) >> C8A(BidU=None, C3pro=None) + C3A(Xiap=None, ParpU=None, C6pro=None), catalysis_1_C8A_catalyzer_C3pro_substrate_C3A_product_1kc)
Rule('catalysis_0_C3A_catalyzer_C6pro_substrate_C6A_product', C3A(Xiap=None, ParpU=None, C6pro=None) + C6pro(C3A=None) | C3A(Xiap=None, ParpU=None, C6pro=1) % C6pro(C3A=1), catalysis_0_C3A_catalyzer_C6pro_substrate_C6A_product_2kf, catalysis_0_C3A_catalyzer_C6pro_substrate_C6A_product_1kr)
Rule('catalysis_1_C3A_catalyzer_C6pro_substrate_C6A_product', C3A(Xiap=None, ParpU=None, C6pro=1) % C6pro(C3A=1) >> C3A(Xiap=None, ParpU=None, C6pro=None) + C6A(C8pro=None), catalysis_1_C3A_catalyzer_C6pro_substrate_C6A_product_1kc)
Rule('catalysis_0_C6A_catalyzer_C8pro_substrate_C8A_product', C6A(C8pro=None) + C8pro(Fadd=None, C6A=None) | C6A(C8pro=1) % C8pro(Fadd=None, C6A=1), catalysis_0_C6A_catalyzer_C8pro_substrate_C8A_product_2kf, catalysis_0_C6A_catalyzer_C8pro_substrate_C8A_product_1kr)
Rule('catalysis_1_C6A_catalyzer_C8pro_substrate_C8A_product', C6A(C8pro=1) % C8pro(Fadd=None, C6A=1) >> C6A(C8pro=None) + C8A(BidU=None, C3pro=None), catalysis_1_C6A_catalyzer_C8pro_substrate_C8A_product_1kc)

Initial(C6A(C8pro=None), C6A_0)
Initial(BaxA(BaxM=None, BaxA_1=None, BaxA_2=None, SmacM=None), BaxA_0)
Initial(Ligand(Receptor=None), Ligand_0)
Initial(C6pro(C3A=None), C6pro_0)
Initial(ParpU(C3A=None), ParpU_0)
Initial(BidU(C8A=None), BidU_0)
Initial(BidT(), BidT_0)
Initial(C3A(Xiap=None, ParpU=None, C6pro=None), C3A_0)
Initial(BidM(BaxM=None), BidM_0)
Initial(BaxM(BidM=None, BaxA=None), BaxM_0)
Initial(C8A(BidU=None, C3pro=None), C8A_0)
Initial(Xiap(SmacC=None, C3A=None), Xiap_0)
Initial(Receptor(Ligand=None, Fadd=None), Receptor_0)
Initial(C3ub(), C3ub_0)
Initial(Fadd(Receptor=None, C8pro=None), Fadd_0)
Initial(C3pro(C8A=None), C3pro_0)
Initial(SmacM(BaxA=None), SmacM_0)
Initial(SmacC(Xiap=None), SmacC_0)
Initial(C8pro(Fadd=None, C6A=None), C8pro_0)
Initial(ParpC(), ParpC_0)

