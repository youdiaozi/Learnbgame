'''
Copyright (C) 2018 SmugTomato

Created by SmugTomato

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

# Vertex coordinate to original normals mapping
neck_normals = [
    # AF
    {
        (0.04542597755789757, 0.016387110576033592, 1.6290936470031738):
            (0.9655436873435974, -0.2602236568927765, -0.002999897813424468),
        (0.043091025203466415, 0.0428246445953846, 1.638722538948059):
            (0.9091801047325134, 0.4057536721229553, 0.09357073903083801),
        (0.025131983682513237, 0.057531364262104034, 1.644945502281189):
            (0.46288588643074036, 0.8730464577674866, 0.15338356792926788),
        (-0.0, 0.06332468241453171, 1.6473431587219238):
            (1.883022150650504e-06, 0.9920651316642761, 0.12572501599788666),
        (-0.025131983682513237, 0.057531364262104034, 1.644945502281189):
            (-0.4628913104534149, 0.873063325881958, 0.15327110886573792),
        (0.03174262121319771, -0.007318969815969467, 1.6197011470794678):
            (0.6254966855049133, -0.7745142579078674, -0.09424198418855667),
        (-0.0, -0.016639504581689835, 1.6158573627471924):
            (4.235032247379422e-05, -0.987336277961731, -0.1586412787437439),
        (0.04542597755789757, 0.016387110576033592, 1.6290936470031738):
            (0.9655436873435974, -0.2602236568927765, -0.002999897813424468),
        (-0.03174262121319771, -0.007318969815969467, 1.6197011470794678):
            (-0.6243377327919006, -0.7754783630371094, -0.0939985141158104),
        (-0.04542597755789757, 0.016387110576033592, 1.6290936470031738):
            (-0.9657487273216248, -0.2594587802886963, -0.0032439199276268482),
        (-0.04542597755789757, 0.016387110576033592, 1.6290936470031738):
            (-0.9657487273216248, -0.2594587802886963, -0.0032439199276268482),
        (-0.043091025203466415, 0.0428246445953846, 1.638722538948059):
            (-0.9096415638923645, 0.40467947721481323, 0.0937376618385315),
    },

    # AM
    {
        (-0.050921496003866196, 0.009695423766970634, 1.6153169870376587):
            (-0.9793702363967896, -0.1899246871471405, 0.06901124864816666),
        (-0.04648229852318764, 0.044279005378484726, 1.6270158290863037):
            (-0.9276052117347717, 0.3034973442554474, 0.21780261397361755),
        (-0.028523258864879608, 0.06441643089056015, 1.63412344455719):
            (-0.434136301279068, 0.8711420297622681, 0.22942808270454407),
        (-0.0, 0.06761889904737473, 1.635151743888855):
            (2.356311767925945e-07, 0.9957233667373657, 0.09238521754741669),
        (0.028523258864879608, 0.06441643089056015, 1.63412344455719):
            (0.43348318338394165, 0.8715948462486267, 0.22894278168678284),
        (0.04648229852318764, 0.044279005378484726, 1.6270158290863037):
            (0.9277547597885132, 0.3034653663635254, 0.2172093242406845),
        (0.050921496003866196, 0.009695423766970634, 1.6153169870376587):
            (0.9792410135269165, -0.19055873155593872, 0.06909748911857605),
        (-0.03740610182285309, -0.02189396508038044, 1.6031373739242554):
            (-0.6604799628257751, -0.7434290051460266, -0.10525917261838913),
        (-0.050921496003866196, 0.009695423766970634, 1.6153169870376587):
            (-0.9793702363967896, -0.1899246871471405, 0.06901124864816666),
        (-0.0, -0.034311868250370026, 1.597963809967041):
            (3.61859638360329e-05, -0.989450991153717, -0.1448681503534317),
        (0.03740610182285309, -0.02189396508038044, 1.6031373739242554):
            (0.6604671478271484, -0.7434564828872681, -0.10514567047357559),
        (0.050921496003866196, 0.009695423766970634, 1.6153169870376587):
            (0.9792410135269165, -0.19055873155593872, 0.06909748911857605)
    },

    # TF
    {
        (-0.04087045416235924, 0.0177291426807642, 1.518518090248108):
            (-0.9648733735084534, -0.2610670328140259, -0.029383135959506035),
        (-0.03876965865492821, 0.044569164514541626, 1.529557704925537):
            (-0.9147070646286011, 0.40135735273361206, 0.04715195670723915),
        (-0.02261163480579853, 0.058393482118844986, 1.5354074239730835):
            (-0.47500374913215637, 0.8710873126983643, 0.1248132586479187),
        (-0.0, 0.06383920460939407, 1.537661075592041):
            (3.3523804177093552e-06, 0.9938828349113464, 0.11043941974639893),
        (0.02261163480579853, 0.058393482118844986, 1.5354074239730835):
            (0.474995493888855, 0.871063232421875, 0.1250123679637909),
        (0.03876965865492821, 0.044569164514541626, 1.529557704925537):
            (0.9141927361488342, 0.40251466631889343, 0.0472610704600811),
        (0.04087045416235924, 0.0177291426807642, 1.518518090248108):
            (0.964704155921936, -0.2617180645465851, -0.029147246852517128),
        (0.028304338455200195, -0.00268368748947978, 1.511141300201416):
            (0.5927016735076904, -0.7986089587211609, -0.1045391783118248),
        (-0.0, -0.009953437373042107, 1.5085225105285645):
            (4.5299206249183044e-05, -0.9942952990531921, -0.10666223615407944),
        (0.04087045416235924, 0.0177291426807642, 1.518518090248108):
            (0.964704155921936, -0.2617180645465851, -0.029147246852517128),
        (-0.028304338455200195, -0.002683687722310424, 1.511141300201416):
            (-0.5914600491523743, -0.7995601892471313, -0.10430033504962921),
        (-0.04087045416235924, 0.0177291426807642, 1.518518090248108):
            (-0.9648733735084534, -0.2610670328140259, -0.029383135959506035)
    },

    # TM
    {
        (-0.035161733627319336, -0.012193472124636173, 1.5085686445236206):
            (-0.6803844571113586, -0.7189215421676636, -0.14222802221775055),
        (-0.047866206616163254, 0.013433256186544895, 1.5194778442382812):
            (-0.9821786284446716, -0.18789365887641907, 0.004590373486280441),
        (-0.0, -0.027933597564697266, 1.5031657218933105):
            (4.722158337244764e-05, -0.9913393259048462, -0.13132552802562714),
        (0.035161733627319336, -0.012193472124636173, 1.5085686445236206):
            (0.680393636226654, -0.7189411520957947, -0.14208507537841797),
        (0.047866206616163254, 0.013433256186544895, 1.5194778442382812):
            (0.9820169806480408, -0.18872983753681183, 0.004870536737143993),
        (-0.047866206616163254, 0.013433256186544895, 1.5194778442382812):
            (-0.9821786284446716, -0.18789365887641907, 0.004590373486280441),
        (-0.043693359941244125, 0.04162226617336273, 1.5293947458267212):
            (-0.9296359419822693, 0.34842273592948914, 0.11991085857152939),
        (-0.026811864227056503, 0.06055144593119621, 1.5360760688781738):
            (-0.4355728328227997, 0.8785452246665955, 0.1960473358631134),
        (-0.0, 0.06356176733970642, 1.5370426177978516):
            (-8.377328413189389e-06, 0.9894232749938965, 0.14505711197853088),
        (0.026811860501766205, 0.060551442205905914, 1.5360760688781738):
            (0.4347971975803375, 0.8790539503097534, 0.19548800587654114),
        (0.043693359941244125, 0.04162226617336273, 1.5293947458267212):
            (0.9297471642494202, 0.3483564555644989, 0.1192392110824585),
        (0.047866206616163254, 0.013433256186544895, 1.5194778442382812):
            (0.9820169806480408, -0.18872983753681183, 0.004870536737143993)
    },

    # CU
    {
        (-0.03456539660692215, -0.011713928543031216, 1.1124541759490967):
            (-0.9897308945655823, -0.12317804992198944, -0.07252537459135056),
        (-0.03155208006501198, 0.011761324480175972, 1.120395541191101):
            (-0.9051440358161926, 0.4246380925178528, 0.019919347018003464),
        (-0.019361523911356926, 0.02543056756258011, 1.1252200603485107):
            (-0.4566517472267151, 0.8869920372962952, 0.06866073608398438),
        (-0.0, 0.027604395523667336, 1.1259181499481201):
            (2.0107568161620293e-06, 0.9970040321350098, 0.07734966278076172),
        (0.019361523911356926, 0.02543056756258011, 1.1252200603485107):
            (0.4557728171348572, 0.8875065445899963, 0.06784697622060776),
        (0.03155208006501198, 0.011761329136788845, 1.120395541191101):
            (0.9052586555480957, 0.42443880438804626, 0.01893235556781292),
        (0.03456539660692215, -0.011713928543031216, 1.1124541759490967):
            (0.9896406531333923, -0.12400682270526886, -0.07234407216310501),
        (0.025391174480319023, -0.033156733959913254, 1.1041866540908813):
            (0.6861978769302368, -0.6767411828041077, -0.2667468786239624),
        (-0.0, -0.041585978120565414, 1.1006748676300049):
            (2.822580972861033e-05, -0.972131609916687, -0.23443587124347687),
        (-0.025391174480319023, -0.033156733959913254, 1.1041866540908813):
            (-0.6863312721252441, -0.6766100525856018, -0.26673632860183716),
        (0.03456539660692215, -0.011713928543031216, 1.1124541759490967):
            (0.9896406531333923, -0.12400682270526886, -0.07234407216310501),
        (-0.03456539660692215, -0.011713928543031216, 1.1124541759490967):
            (-0.9897308945655823, -0.12317804992198944, -0.07252537459135056)
    },

    # PU
    {
        (-0.029718322679400444, -0.009239223785698414, 0.6809873580932617):
            (-0.9797395467758179, -0.19932131469249725, -0.019529012963175774),
        (-0.02839687280356884, 0.008840582333505154, 0.6872459053993225):
            (-0.9096804261207581, 0.41466888785362244, 0.023048201575875282),
        (-0.01742537133395672, 0.020249394699931145, 0.6899859309196472):
            (-0.4433377683162689, 0.8935477137565613, -0.07088051736354828),
        (-1.8809112253825866e-11, 0.022063741460442543, 0.6902136206626892):
            (9.747302556206705e-07, 0.9912765622138977, -0.1317981332540512),
        (0.01742537133395672, 0.020249394699931145, 0.6899859309196472):
            (0.4423581063747406, 0.8939225077629089, -0.07226219028234482),
        (0.02839687280356884, 0.008840583264827728, 0.6872459053993225):
            (0.9098556041717529, 0.41436368227005005, 0.02157682180404663),
        (0.029718318954110146, -0.009239223785698414, 0.6809873580932617):
            (0.9795541167259216, -0.20027871429920197, -0.019031163305044174),
        (-0.021241536363959312, -0.025106849148869514, 0.67401123046875):
            (-0.69950270652771, -0.6890288591384888, -0.18956582248210907),
        (-0.029718322679400444, -0.009239223785698414, 0.6809873580932617):
            (-0.9797395467758179, -0.19932131469249725, -0.019529012963175774),
        (-1.8809112253825866e-11, -0.03434498608112335, 0.6700497269630432):
            (3.682478200062178e-05, -0.9808242321014404, -0.19489434361457825),
        (0.021241825073957443, -0.025106851011514664, 0.6740112900733948):
            (0.699383020401001, -0.6891916990280151, -0.18941543996334076),
        (0.029718318954110146, -0.009239223785698414, 0.6809873580932617):
            (0.9795541167259216, -0.20027871429920197, -0.019031163305044174)
    }
]
