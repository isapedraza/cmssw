import FWCore.ParameterSet.Config as cms

HBHENoiseFilterResultProducer = cms.EDProducer(
    'HBHENoiseFilterResultProducer',
    noiselabel = cms.InputTag('hcalnoise'),
    minHPDHits = cms.int32(17),
    minHPDNoOtherHits = cms.int32(10),
    minZeros = cms.int32(10),
    IgnoreTS4TS5ifJetInLowBVRegion = cms.bool(True),
    defaultDecision = cms.string("HBHENoiseFilterResultRun1")
)

from Configuration.StandardSequences.Eras import eras
eras.run2_common.toModify(HBHENoiseFilterResultProducer, IgnoreTS4TS5ifJetInLowBVRegion=False)
eras.run2_common.toModify(HBHENoiseFilterResultProducer, defaultDecision="HBHENoiseFilterResultRun2Loose")
