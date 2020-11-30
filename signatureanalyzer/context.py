import itertools

# Cartesian product for 96 SNV
acontext = itertools.product('A', 'CGT', 'ACGT', 'ACGT')
ccontext = itertools.product('C', 'AGT', 'ACGT', 'ACGT')

# Cartesian product for 1536 SNV Arrow
t_1536 = itertools.product('ACGT','ACGT','[','T','>','ACG',']','ACGT','ACGT')
c_1536 = itertools.product('ACGT','ACGT','[','C','>','AGT',']','ACGT','ACGT')

t_1536_word = itertools.product('T', 'ACG', 'ACGT', 'ACGT', 'ACGT', 'ACGT')
c_1536_word = itertools.product('C', 'AGT', 'ACGT', 'ACGT', 'ACGT', 'ACGT')

# Define dictionary for all contexts
context96 = dict(zip(map(''.join, itertools.chain(acontext, ccontext)), range(1, 97)))
context1536 = dict(zip(map(''.join, itertools.chain(t_1536, c_1536)), range(1, 1537)))
context1536_word = dict(zip(map(''.join, itertools.chain(t_1536_word, c_1536_word)), range(1, 1537)))
context78 = dict(zip(['AC>CA', 'AC>CG', 'AC>CT', 'AC>GA', 'AC>GG', 'AC>GT', 'AC>TA', 'AC>TG', 'AC>TT', 'AT>CA',
                      'AT>CC', 'AT>CG', 'AT>GA', 'AT>GC', 'AT>TA', 'CC>AA', 'CC>AG', 'CC>AT', 'CC>GA', 'CC>GG',
                      'CC>GT', 'CC>TA', 'CC>TG', 'CC>TT', 'CG>AT', 'CG>GC', 'CG>GT', 'CG>TA', 'CG>TC', 'CG>TT',
                      'CT>AA', 'CT>AC', 'CT>AG', 'CT>GA', 'CT>GC', 'CT>GG', 'CT>TA', 'CT>TC', 'CT>TG', 'GC>AA',
                      'GC>AG', 'GC>AT', 'GC>CA', 'GC>CG', 'GC>TA', 'TA>AT', 'TA>CG', 'TA>CT', 'TA>GC', 'TA>GG',
                      'TA>GT', 'TC>AA', 'TC>AG', 'TC>AT', 'TC>CA', 'TC>CG', 'TC>CT', 'TC>GA', 'TC>GG', 'TC>GT',
                      'TG>AA', 'TG>AC', 'TG>AT', 'TG>CA', 'TG>CC', 'TG>CT', 'TG>GA', 'TG>GC', 'TG>GT', 'TT>AA',
                      'TT>AC', 'TT>AG', 'TT>CA', 'TT>CC', 'TT>CG', 'TT>GA', 'TT>GC', 'TT>GG'], range(1, 79)))

context83 = dict(zip(['Cdel1', 'Cdel2', 'Cdel3', 'Cdel4', 'Cdel5', 'Cdel6+',
                       'Tdel1', 'Tdel2', 'Tdel3', 'Tdel4', 'Tdel5', 'Tdel6+',
                       'Cins0', 'Cins1', 'Cins2', 'Cins3', 'Cins4', 'Cins5+',
                       'Tins0', 'Tins1', 'Tins2', 'Tins3', 'Tins4', 'Tins5+',
                       '2del1', '2del2', '2del3', '2del4', '2del5', '2del6+',
                       '3del1', '3del2', '3del3', '3del4', '3del5', '3del6+',
                       '4del1', '4del2', '4del3', '4del4', '4del5', '4del6+',
                       '5+del1', '5+del2', '5+del3', '5+del4', '5+del5', '5+del6+',
                       '2ins0', '2ins1', '2ins2', '2ins3', '2ins4', '2ins5+',
                       '3ins0', '3ins1', '3ins2', '3ins3', '3ins4', '3ins5+',
                       '4ins0', '4ins1', '4ins2', '4ins3', '4ins4', '4ins5+',
                       '5+ins0', '5+ins1', '5+ins2', '5+ins3', '5+ins4', '5+ins5+',
                       '2delm1', '3delm1', '3delm2', '4delm1', '4delm2', '4delm3',
                       '5+delm1', '5+delm2', '5+delm3', '5+delm4', '5+delm5+'], range(1, 84)))
context_composite = {**context1536, **({k:v+1536 for k,v in context78.items()}), **({k:v+1614 for k,v in context83.items()})}

signature_composite = {'SBS1':'Deamination of 5-methylcytosine (Aging)',
                       'SBS2':'APOBEC activity',
                       'SBS3':'Defective HR',
                       'SBS4':'Tobacco Smoking',
                       'SBS5':'Unknown (clock-like)',
                       'SBS6':'Defective DNA mismatch repair',
                       'SBS7a':'Ultraviolet light exposure',
                       'SBS7b':'Ultraviolet light exposure',
                       'SBS7c':'Ultraviolet light exposure',
                       'SBS8':'Unknown-8',
                       'SBS9':'Polymerase eta activity',
                       'SBS10a':'POLE mutation',
                       'SBS11':'Temozolomide treatment',
                       'SBS12':'Unknown-12: Predominant in liver',
                       'SBS13':'APOBEC activity',
                       'SBS14':'Defective mismatch repair + POLE mutation',
                       'SBS15':'Defective mismatch repair',
                       'SBS16':'Unknown-16',
                       'SBS17a':'Unknown-17a',
                       'SBS17b':'Unknown-17b',
                       'SBS18':'Reactive oxygen species',
                       'SBS19':'Unknown-19',
                       'SBS21':'Defective mismatch repair',
                       'SBS22':'Aristolochic acid exposure',
                       'SBS26':'Defective mismatch repair',
                       'SBS28':'Unknown-28 (Associated with POLE 10a/10b)',
                       'SBS30':'Defective DNA base excision repair (NTHL1 mutation)',
                       'SBS33':'Unknown-33',
                       'SBS35':'Platinum treatment',
                       'SBS36':'Defective base excision repair',
                       'SBS37':'Predominant in Prostate',
                       'SBS38':'Indirect effect of ultraviolet light',
                       'SBS39':'Unknown-39',
                       'SBS40':'Predominant in Kidney',
                       'SBS44':'Defective mismatch repair',
                       'SBS55':'Ultraviolet light exposure',
                       'SBS60':'Artifact mode',
                       'SBS61':'Polymerase epsilon mutation',
                       'SBS62':'Polymerase epsilon mutation',
                       'SBS63':'Polymerase epsilon mutation',
                       'SBS64':'SBS15_0.63, ID1(1.0) - ID driven (DNA mismatch repair)',
                       'SBS65':'Ultraviolet light exposure',
                       'SBS66':'Polymerase epsilon mutation',
                       'SBS67':'Ultraviolet light exposure',
                       'SBS68':'SBS7a_0.86 (UV light exposure)',
                       'SBS69':'APOBEC3B-like activity',
                       'SBS70':'SBS40_0.71 (Unknown-correlated with age)',
                       'SBS71':'SBS1_0.64, ID2(1.0) - ID driven (Aging)',
                       'SBS72':'SBS9_0.63; Enriched in Lymph-BNHL',
                       'SBS73':'Defective mismatch repair; SBS21(.75),ID7(.96)+POLD(?)',
                       'SBS74':'SBS1-like in Defective mismatch repair samples',
                       'SBS75':'Ultraviolet light exposure',
                       'SBS76':'Defective mismatch repair - ID driven',
                       'SBS77':'Associated with BI_ID14(1.0) - ID driven',
                       'SBS78':'Polymerase epsilon mutation - SBS28-like',
                       'SBS79':'Defective mismatch repair',
                       'SBS80':'Predominant in Prostate',
                       'SBS81':'SBS35(0.52),ID4(0.92) - ID driven',
                       'SBS82':'SBS3_0.74, ID11(1.0) - ID driven',
                       'SBS83':'Unknown-83'}

signature_cosmic = {'SBS1':'Deamination of 5-methylcytosine',
                'SBS2':'APOBEC activity',
                'SBS3':'Defective HR',
                'SBS4':'Tobacco Smoking',
                'SBS5':'Unknown (clock-like)',
                'SBS6':'Defective DNA mismatch repair',
                'SBS7a':'Ultraviolet light exposure',
                'SBS7b':'Ultraviolet light exposure',
                'SBS7c':'Ultraviolet light exposure',
                'SBS7d':'Ultraviolet light exposure',
                'SBS8':'Unknown-8',
                'SBS9':'Polymerase eta somatic hypermutation activity',
                'SBS10a':'POLE exonuclease domain mutation',
                'SBS10b':'POLE exonuclease domain mutation',
                'SBS11':'Temozolomide treatment',
                'SBS12':'Unknown-12 (Predominant in liver)',
                'SBS13':'APOBEC activity',
                'SBS14':'Defective mismatch repair + POLE mutation',
                'SBS15':'Defective mismatch repair',
                'SBS16':'Unknown-16',
                'SBS17a':'Unknown-17a',
                'SBS17b':'Unknown-17b (fluorouracil chemotherapy and reactive oxygen species)',
                'SBS18':'Reactive oxygen species',
                'SBS19':'Unknown-19',
                'SBS21':'Concurrent POLD1 mutations and defective mismatch repair',
                'SBS21':'Defective mismatch repair',
                'SBS22':'Aristolochic acid exposure',
                'SBS23':'Unknown-23',
                'SBS24':'Aflatoxin exposure',
                'SBS25':'Chemotherapy treatment',
                'SBS26':'Defective mismatch repair',
                'SBS27':'Sequencing artefact',
                'SBS28':'Unknown-28 (Associated with POLE SBS10a/10b)',
                'SBS29':'Tobacco Chewing',
                'SBS30':'Defective DNA base excision repair (NTHL1 mutation)',
                'SBS31':'Platinum chemotherapy treament',
                'SBS32':'Azathioprine treatment',
                'SBS33':'Unknown-33',
                'SBS34':'Unknown-34',
                'SBS35':'Platinum chemotherapy treatment',
                'SBS36':'Defective base excision repair (MUTYH mutations)',
                'SBS37':'Unknown-37',
                'SBS38':'Indirect effect of ultraviolet light',
                'SBS39':'Unknown-39',
                'SBS40':'Unknown-40',
                'SBS41':'Unknown-41',
                'SBS42':'Haloalkane exposure',
                'SBS43':'Sequencing artefact',
                'SBS44':'Defective mismatch repair',
                'SBS45':'Sequencing artefact-45',
                'SBS46':'Sequencing artefact-46',
                'SBS47':'Sequencing artefact-47',
                'SBS48':'Sequencing artefact-48',
                'SBS49':'Sequencing artefact-49',
                'SBS50':'Sequencing artefact-50',
                'SBS51':'Sequencing artefact-51',
                'SBS52':'Sequencing artefact-52',
                'SBS53':'Sequencing artefact-53',
                'SBS54':'Sequencing artefact-54',
                'SBS55':'Sequencing artefact-55',
                'SBS56':'Sequencing artefact-56',
                'SBS57':'Sequencing artefact-57',
                'SBS58':'Sequencing artefact-58',
                'SBS59':'Sequencing artefact-59',
                'SBS60':'Sequencing artefact-60',
                'SBS84':'Activity of activation-induced cytidine deaminase (AID)',
                'SBS85':'Indirect effects of activation-induced cytidine deaminase (AID)',
                'SBS86':'Unknown chemotherapy treatment',
                'SBS87':'Thiopurine chemotherapy treatment',
                'SBS88':'Colibactin exposure',
                'SBS89':'Unknown-89',
                'SBS90':'Duocarmycin exposure'
                }
signature_DBS = {'DBS1':'Ultraviolet light exposure',
                 'DBS2':'Tobacco smoking and other mutagens',
                 'DBS3':'Polymerase epsilon exonuclease domain mutations',
                 'DBS4':'Unknown-4',
                 'DBS5':'Platinum chemotherapy treatment',
                 'DBS6':'Unknown-6',
                 'DBS7':'Defective mismatch repair',
                 'DBS8':'Unknown-8',
                 'DBS9':'Unknown-9',
                 'DBS10':'Defective mismatch repair',
                 'DBS11':'Unknown (possibly related to APOBEC mutagenesis'
                 }
signature_ID = {'ID1':'Slippage during DNA replication of the replicated DNA strand',
                'ID2':'Slippage during DNA replication of the replicated DNA strand',
                'ID3':'Tobacco smoking',
                'ID4':'Unknown-4',
                'ID5':'Unknown-5',
                'ID6':'Defective homologous recombination-based DNA damage repair',
                'ID7':'Defective mismatch repair',
                'ID8':'Repaire of double strand breaks by non-homologous end-joining mechanisms or mutations in topoisomerase TOP2A',
                'ID9':'Unknown-9',
                'ID10':'Unknown-10',
                'ID11':'Unknown-11',
                'ID12':'Unknown-12',
                'ID13':'Ultraviolet light exposure',
                'ID14':'Unknown-14',
                'ID15':'Unknown-15',
                'ID16':'Unknown-16',
                'ID17':'Mutations in topoisomerase TOP2A',
                'ID18':'Colibactin exposure'
                }
