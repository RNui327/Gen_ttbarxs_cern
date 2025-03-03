Needs["QQbarThreshold`"];

strm=OpenWrite["/afs/cern.ch/user/l/linyu/private/gen_ttbarxs_cern-main/test/submit/result/mass171.5150.txt"];
AppendTo[$Output,strm];

LoadGrid[GridDirectory <> "ttbar_grid.tsv"];
With[
   {
     mu = 80.,
     mtPS = 171.5,
     muWidth = 350.,
     width = 1.33,
     order = "N3LO",
     energyw=1,
     kew = 1.00,
     alphas = 0.1184
   },
   With[
      {sqrtsinit = 340},      
Do[
       delwidth=0;
       delmass=0.0150;
       sqrts=sqrtsinit+energy;
       ewidth=kew*0.51*sqrts*sqrts/360/360;
       beta=ISRLog[sqrts, alphamZ];
       xmin = (330./sqrts)^2;
       tmax = (1-xmin)^beta;
         Print[mtPS+delmass, "\t", width+delwidth, "\t", alphas, "\t", sqrts, "\t",
   1000*NIntegrate[
      ModifiedLuminosityFunction[t, beta]*
      (1 / ewidth / Sqrt[ 2*3.1415926 ] * Exp[ -(sqrts-ss)*(sqrts-ss) / 2 / ewidth / ewidth ] )*
      TTbarXSection[
               Sqrt[1-t^(1/beta)] * ss, {mu, muWidth}, {mtPS+delmass, width+delwidth}, order,
ISRConst->True, 
alphaSmZ -> alphas           
 ],
      {ss, 330, 370},
      {t, 0, tmax}
         ]
      ],
{energy, 0., 6., 0.25}
   ]
]
];
Close[strm]
