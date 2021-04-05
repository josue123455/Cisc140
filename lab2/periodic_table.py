class Periodic_Table:
    def __init__(self, atomic_number,	name,	symbol,	group,	period,	element_category,	atomic_weight,	phase):
        self._1 = Hydrogen ("1, Hydrogen,	H,	1,	1,	diatomic_nonmetal,	1.008,	gas")
        self._2 = Heluim ("2,Helium, He, 18,	1,	noble_gas,	4.0026022,	gas")
        self._3 = Lithuim ("3, Lithium,	Li,	1,	2,	alkali_metal,	6.94,	solid")
        self._4 = Beryllium ("4,	Beryllium,	Be,	2,	2,	alkaline_earth_metal,	9.01218315,	solid")
        self._5 = Boron ("5,Boron,	B,	13,	2,	metalloid,	10.81,	solid")
        self._6 =Carbon ("6,Carbon,	C,	14,	2,	polyatomic_nonmetal,12.011,	solid")
        self._7 = Nitrogen("7,Nitrogen,	N,	15,	2,	diatomic_nonmetal,	14.007,	gas")
        self._8 =Oxygen ("8,	Oxygen,	O,	16,	2,	diatomic_nonmetal,15.999,	gas")
        self._9 =Fluorine ("9,Fluorine,	F,17,2,	diatomic_nonmetal,	18.99840316,	gas")
        self._10 = Neon("10,	Neon,	Ne,	18,	2,	noble-gas,	20.17976,	gas")
        self._11 =Sodium ("11,	Sodium,	Na,	1,	3,alkali_metal,	22.98976928,	solid")
        self._12 =Magnesium ("12,Magnesium,	Mg,	2,	3,	alkaline-earth-metal,	24.305,	solid")
        self._13 =Aluminum ("13,	Aluminum,	Al,	13,	3,	post-transition-metal,	26.98153857,	solid")
        self._14 =Silicon ("14,	Silicon,	Si,	14,	3,	metalloid,	28.085,	solid")
        self._15 =Phosphorus ("15,	Phosphorus,	P,	15,	3,	polyatomic_nonmetal,	30.973762,	solid")
        self._16 =Sulfur ("16,	Sulfur,	S,	16,	3,	polyatomic-nonmetal,	32.06,	solid")
        self._17 = Chlorine ("17,	Chlorine,	Cl,	17,	3,	diatomic-nonmetal,	35.45,	gas")
        self._18 =Argon("18,	Argon,	Ar,	18,	3,	noble_gas,	39.9481,	gas")
        self._19 =Potassium ("19,	Potassium,	K,	1,	4,	alkali_metal,	39.09831,	solid")
        self._20 =Calcium ("20,	Calcium,	Ca,	2,	4,	alkaline_earth_metal,	40.0784,	solid")
        self._21 =Scandium ("21,	Scandium,	Sc,	3,	4,	transition_metal,	44.9559085,	solid")
        self._22 =Titanium("22,	Titanium,	Ti,	4,	4,	transition_metal,	47.8671,	solid")
        self._23 =Vanadium("23,	Vanadium,	V,	5,	4,	transition_metal,	50.94151,	solid")
        self._24 =Chromium("24,	Chromium,	Cr,	6,	4,	transition_metal,	51.99616,	solid")
        self._25 =Manganese ("25,	Manganese,	Mn,	7,	4,	transition_metal,	54.9380443,	solid")
        self._26 = Iron ("26,	Iron,	Fe,	8,	4,	transition_metal,	55.8452,	solid")
        self._27 =Cobalt ("27,	Cobalt,	Co,	9,	4,	transition_metal,	58.9331944,	solid")
        self._28 =Nickel ("28,	Nickel,	Ni,	10,	4,	transition_metal,	58.69344,	solid")
        self._29= Copper ("29,	Copper,	Cu,	11,	4,	transition_metal,	63.5463	,solid")
        self._30 =Zinc ("30,	Zinc,	Zn,	12,	4,	transition_metal,	65.382,	solid")
        self._31 =Gallium ("31,	Gallium,	Ga,	13,	4,	post-transition_metal,	69.7231,	solid")
        self._32 =Germanium ("32,	Germanium,	Ge,	14,	4,	metalloid,	72.6308,	solid")
        self._33 =Arsenic ("33,	Arsenic,	As,	15,	4,	metalloid,	74.9215956,	solid")
        self._34 =Selenium ("34,	Selenium,	Se,	16,	4,	polyatomic_nonmetal,	78.9718,	solid")
        self._35 =Bromine("35,	Bromine,	Br,	17,	4,	diatomic_nonmetal,	79.904,	liquid")
        self._36 =Krypton ("36,	Krypton,	Kr,	18,	4,	noble_gas,	83.7982,	gas")
        self._37 = Rubidium ("37,	Rubidium,	Rb,	1,	5,	alkali_metal,	85.46783,	solid")
        self._38 = Strontium ("38,	Strontium,	Sr,	2,	5,	alkaline_earth_metal,	87.621,	solid")
        self._39 = Yttrium ("39,	Yttrium,	Y,	3,	5,	transition_metal,	88.905842,	solid")
        self._40 = Zirconium("40,	Zirconium,	Zr,	4,	5,	transition_metal,	91.2242,	solid")
        self._41 = Niobium("41,	Niobium,	Nb,	5,	5,	transition_metal,	92.906372,	solid")
        self._42 = Molybdenum ("42,	Molybdenum,	Mo,	6,	5,	transition_metal,	95.951,	solid")
        self._43 = Technetium ("43,	Technetium,	Tc,	7,	5,	transition_metal,	98,	solid")
        self._44 = Ruthenium ("44,	Ruthenium,	Ru,	8,	5,	transition_metal,	101.072	")
        self._45 = Rhodium("45,	Rhodium,	Rh,	9,	5,	transition_metal,	102.905502,	solid")
        self._46 = Palladium ("46,	Palladium,	Pd,	10,	5,	transition_metal,	106.421,	solid")
        self._47 = Silver ("47,	Silver,	Ag,	11,	5,	transition_metal,	107.86822,	solid")
        self._48 = Cadmium("48,	Cadmium,	Cd,	12,	5,	transition_metal,	112.4144,	solid")
        self._49 = Indium("49,	Indium,	In,	13,	5,	post-transition-metal,	114.8181,	solid")
        self._50 = Tin("50,	Tin,	Sn,	14,	5,	post-transition_metal,	118.7107,	solid")
        self._51 = Antimony("51,	Antimony,	Sb,	15,	5,	metalloid,	121.7601,	solid")
        self._52 = Tellurium("52,	Tellurium,	Te,	16,	5,	metalloid,	127.603,	solid")
        self._53 = Iodine("53,	Iodine,	I,	17,	5,	diatomic_nonmetal,	126.904473,	solid")
        self._54 = Xenon("54,	Xenon,	Xe,	18,	5,	noble_gas,	131.2936,	gas")
        self._55 = Cesium("55,	Cesium,	Cs,	1,	6,	alkali_metal,	132.905452,	solid")
        self._56 = Barium("56,	Barium,	Ba,	2,	6,	alkaline_earth_metals,	137.3277,	solid")
        self._57 = Lanthanum("57,	Lanthanum,	La,	3,	6,	lanthanide,	138.905477,	solid")
        self._58 = Cerium("57,	Lanthanum,	La,	3,	6,	lanthanide,	138.905477,	solid")
        self._59 =Praseodymium("58,	Cerium,	Ce,	n/a,	6,	lanthanide,	140.1161,	solid")
        self._60 = Neodymium("59,	Praseodymium,	Pr,	n/a	,6,	lanthanide,	140.907662,	solid")
        self._61 = Promethium("61,	Promethium,	P,m	n/a,	6,	lanthanide,	145,	solid")
        self._62 =Samarium("62,	Samarium,	Sm,	n/a,	6,	lanthanide,	150.362,	solid")
        self._63 =Europium("63,	Europium,	Eu,	n/a,	6,	lanthanide,	151.9641,	solid")
        self._64 =Gadolinium("64,	Gadolinium,	Gd,	n/a,	6,	lanthanide,	157.253	,solid")
        self._65 =Terbium("65,	Terbium,	Tb,	n/a,	6,	lanthanide,	158.925352	,solid")
        self._66 =Dysprosium("66,	Dysprosium,	Dy,	n/a,	6,	lanthanide,	162.5001,	solid")
        self._67 =Holmium("67,	Holmium	,Ho,	n/a,6,	lanthanide,	164.930332,	solid")
        self._68 = Erbium("68,	Erbium,	Er,	n/a,	6,	lanthanide,	167.2593,	solid")
        self._69 = Thulium("69,	Thulium,	Tm,	n/a,6,	lanthanide,	168.934222,	solid")
        self._70 = Ytterbium("70,	Ytterbium,	Yb,	n/a	,6,	lanthanide,	173.0451,	solid")
        self._71 = Lutetium("71,	Lutetium,	Lu,	n/a,	6,	lanthanide,	174.96681,	solid")
        self._72 = Hafnium("72,	Hafnium,	Hf,	4,	6,	transition_metal,	178.492	,solid")
        self._73 = Tantalum("73,	Tantalum,	Ta,	5,	6,	transition_metal,	180.947882,	solid")
        self._74 = Tungsten("74,	Tungsten,	W,	6,	6,	transition_metal,	183.841,	solid")
        self._75 = Rhenium("75,	Rhenium,	Re,	7,	6,	transition_metal,	186.2071,	solid")
        self._76 = Osmium("76,	Osmium,	Os,	8,	6,	transition_metal,	190.233,	solid")
        self._77 = Iridium("77,	Iridium,	Ir,	9,	6,	transition_metal,	192.2173,	solid")
        self._78 = Platinum("78	,Platinum,	Pt,	10,	6,	transition_metal,	195.0849,	solid")
        self._79 = Gold("79,	Gold,	Au,	11,	6,	transition_metal,	196.9665695,	solid")
        self._80 = Mercury("80,	Mercury,	Hg,	12,	6,	transition_metal,	200.5923,	liquid")
        self._81 = Thallium("81,	Thallium,	Tl,	13,	6,	post-transition_metal,	204.38,	solid")
        self._82 = Lead("82,	Lead,	Pb,	14,	6,	post-transition_metal,	207.21,	solid")
        self._83 =Bismuth("83,	Bismuth,	Bi,	15,	6,	post-transition_metal,	208.980401,	solid")
        self._84 = Polonium("84,	Polonium,	Po,	16,	6,	post-transition_metal,	209	,solid")
        self._85 = Astatine("85,	Astatine,	At,	17,	6,	metalloid,	210,	solid")
        self._86 = Radon("86,	Radon,	Rn,	18,	6,	noble_gas,	222	,gas")
        self._87 = Francium("87	,Francium,	Fr,	1,	7,	alkali_metal,	223	,solid presumably")
        self._88 = Radium("88,	Radium,	Ra,	2,	7,	alkaline_earth_metal,	226,	solid")
        self._89 = Actinium("89	,Actinium,	Ac,	3,	7,	actinide,	227,	solid")
        self._90 = Thorium("90,	Thorium,	Th,	n/a,	7,	actinide,	232.03774,	solid")
        self._91 = Protactinium("91,	Protactinium,	Pa,	n/a	,7,	actinide,	231.035882,	solid")
        self._92 = Uranium("92,	Uranium,	U,	n/a,	7,	actinide,	238.028913,	solid")
        self._93 = Neptunium("93,	Neptunium,	Np,	n/a,	7,	actinide,	237	,solid")
        self._94 = Plutonium("94,	Plutonium,	Pu,	n/a,	7,	actinide,	244,	solid")
        self._95 = Americium("95,	Americium,	Am,	n/a,	7,	actinide,	243,	solid")
        self._96 = Curium("96,	Curium,	Cm,	n/a,	7,	actinide,	247,	solid")
        self._97 = Berkelium("97,	Berkelium,	Bk,	n/a,	7,	actinide,	247,solid")
        self._98 = Californium("98,	Californium,	Cf,	n/a,	7,	actinide,	251,	solid")
        self._99 = Einsteinium("99,	Einsteinium,	Es,	n/a,	7,	actinide,	252,	solid")
        self._100 = Fermium("100,	Fermium,	Fm,	n/a	,7,	actinide,	257	,solid_(predicted)")
        self._101 = Mendelevium("101,	Mendelevium,	Md,	n/a,	7,	actinide,	258	,solid_(predicted)")
        self._102 = Nobelium("102,	Nobelium,	No,	n/a,	7,	actinide,	259,	solid_(predicted)")
        self._103 = Lawrencium("103,	Lawrencium,	Lr,	n/a,	7,	actinide,	266,	solid_(predicted)")
        self._104 = Rutherfordium("104,	Rutherfordium,	Rf,	4,	7,	transition-metal,	267,	solid_(predicted)")
        self._105 = Dubnium("105,	Dubnium	,Db,	5,	7,	transition_metal,	268,	solid_(predicted)")
        self._106 = Seaborgium("106,	Seaborgium,	Sg,	6,	7,	transition_metal,	269,solid_(predicted)")
        self._107 = Bohrium("107,	Bohrium,	Bh,	7,	7,	transition_metal,	270,	solid-(predicted)")
        self._108 = Hassium("108,	Hassium,	Hs,	8,	7,	transition_metal,	269,	solid_(predicted)")
        self._109 = Meitnerium("109,	Meitnerium,	Mt,	9,	7,	unknown,	278,	solid_(predicted)")
        self._110 = Darmstadtium("110,	Darmstadtium,	Ds,	10,	7,	unknown,	281,	solid_(predicted)")
        self._111 = Roentgenium("111,	Roentgenium,	Rg,	11,	7,	unknown,	282,	solid_(predicted)")
        self._112 = Copernicium("112,	Copernicium,	Cn,	12,	7,	unknown,	285,	gas_(predicted)")
        self._113 = Nihonium("113,	Nihonium,	Nh,	13,	7,	unknown,	286,	solid_(predicted)")
        self._114 = Flerovium("114,	Flerovium,	Fl,	14,	7,	unknown,	289,	solid_(predicted)")
        self._115 = Moscovium("115,	Moscovium,	Mc,	15,	7,	unknown,	289,	solid_(predicted)")
        self._116 = Livermorium("116,	Livermorium,	Lv,	16,	7,	unknown,	293	,solid_(predicted)")
        self._117 = Tennessine("117,	Tennessine,	Ts,	17,	7,	unknown,	294,	solid_(predicted)")
        self._118 = Oganesson("118,	Oganesson,	Og,	18,	7,	unknown,	294	,solid_(predicted)")

    def get_atomic_number(self):
        return self._atomic_number

    def get_name(self):
        return self._name

    def get_symbol(self):
        return self._symbol

    def get_group(self):
        if self._group is None:

            return "element has no group"
        else:
            return self._group


    def get_period(self):
        return self._period



    def get_element_category(self):
        return self._element_category

    def get_atomic_weight(self):
        return self._atomic_weight

    def get_phase(self):
        return self._phase

if __name__ == '__main__':
    main()

#python periodic_table.py - test
