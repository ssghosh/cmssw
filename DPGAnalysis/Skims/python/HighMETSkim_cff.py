import FWCore.ParameterSet.Config as cms


## select events with at least one good PV
from RecoMET.METFilters.primaryVertexFilter_cfi import *

## apply HBHE Noise filter
## import CommonTools.RecoAlgos.HBHENoiseFilter_cfi
## HBHENoiseFilter = CommonTools.RecoAlgos.HBHENoiseFilter_cfi.HBHENoiseFilter.clone()


## select events with high pfMET
pfMETSelectorHighMETSkim = cms.EDFilter(
    "CandViewSelector",
    src = cms.InputTag("pfMet"),
    cut = cms.string( "pt()>200" )
    )

pfMETCounterHighMETSkim = cms.EDFilter(
    "CandViewCountFilter",
    src = cms.InputTag("pfMETSelectorHighMETSkim"),
    minNumber = cms.uint32(1),
    )

pfMETSelSeq = cms.Sequence(
			   primaryVertexFilter*
                           ##HBHENoiseFilter*
                           pfMETSelectorHighMETSkim*
                           pfMETCounterHighMETSkim
                           )



## select events with high caloMET
caloMETSelectorHighMETSkim = cms.EDFilter(
    "CandViewSelector",
    src = cms.InputTag("caloMetM"),
    cut = cms.string( "pt()>200" )
    )

caloMETCounterHighMETSkim = cms.EDFilter(
    "CandViewCountFilter",
    src = cms.InputTag("caloMETSelectorHighMETSkim"),
    minNumber = cms.uint32(1),
    )

caloMETSelSeq = cms.Sequence(
			   primaryVertexFilter*
                           ##HBHENoiseFilter*
                           caloMETSelectorHighMETSkim*
                           caloMETCounterHighMETSkim
                           )


## select events with high MET dependent on PF and Calo MET Conditions
CondMETSelectorHighMETSkim = cms.EDProducer(
   "CandViewShallowCloneCombiner",
   decay = cms.string("pfMet caloMetM"),
   cut = cms.string(" (daughter(0).pt > 200) || (daughter(0).pt/daughter(1).pt > 2 && daughter(1).pt > 150 ) || (daughter(1).pt/daughter(0).pt > 2 && daughter(0).pt > 150 )  " )
   )

CondMETCounterHighMETSkim = cms.EDFilter(
    "CandViewCountFilter",
    src = cms.InputTag("CondMETSelectorHighMETSkim"),
    minNumber = cms.uint32(1),
    )

CondMETSelSeq = cms.Sequence(
                           primaryVertexFilter*
                           ##HBHENoiseFilter*
                           CondMETSelectorHighMETSkim*
                           CondMETCounterHighMETSkim
                           )



## select events with PAT METs in MINIAODSIM - remember to keep the right branches in the cmsDriver
miniMETSelectorHighMETSkim = cms.EDFilter(
    "CandViewSelector",
    src = cms.InputTag("slimmedMETs"),
    cut = cms.string( "pt()>200" )
    )

miniMETCounterHighMETSkim = cms.EDFilter(
    "CandViewCountFilter",
    src = cms.InputTag("miniMETSelectorHighMETSkim"),
    minNumber = cms.uint32(1),
    )

miniMETSelSeq = cms.Sequence(
                           ##HBHENoiseFilter*
                           miniMETSelectorHighMETSkim*
                           miniMETCounterHighMETSkim
                           )

