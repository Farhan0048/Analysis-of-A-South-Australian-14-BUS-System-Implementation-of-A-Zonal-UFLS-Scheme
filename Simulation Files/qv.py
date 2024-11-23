# File:"C:\Users\ASUS\Desktop\Without battery 6 machine\4_mach_renew.py", generated on SAT, APR 13 2019  11:36, PSS(R)E release 34.03.02

psspy.case(r"""F:\PS project\shz\qv_new.sav""")
gen=600.0/4
ic = 650
proposed = 0
psspy.machine_data_2(315,r"""1""",[_i,_i,_i,_i,_i,_i],[ ic, 31.3124, 150.0,-150.0, 666.66,0.0, 700,_f, 0.17,_f,_f,_f,_f,_f,_f,_f,_f])
psspy.machine_data_2(502,r"""1""",[_i,_i,_i,_i,_i,_i],[ gen, 6.3124, 150.0,-150.0, 300.0,0.0, 300,_f, 0.22,_f,_f,_f,_f,_f,_f,_f,_f])
psspy.machine_data_2(502,r"""2""",[_i,_i,_i,_i,_i,_i],[ gen, 6.3124, 150.0,-150.0, 200,0.0, 300,_f, 0.22,_f,_f,_f,_f,_f,_f,_f,_f])
psspy.machine_data_2(502,r"""3""",[_i,_i,_i,_i,_i,_i],[ gen, 6.3124, 150.0,-150.0, 200,0.0, 300,_f, 0.22,_f,_f,_f,_f,_f,_f,_f,_f])
psspy.machine_data_2(502,r"""4""",[_i,_i,_i,_i,_i,_i],[ gen, 6.3124, 150.0,-150.0, 200,0.0, 300,_f, 0.22,_f,_f,_f,_f,_f,_f,_f,_f])
psspy.machine_data_2(502,r"""5""",[_i,_i,_i,_i,_i,_i],[ gen, 6.3124, 150.0,-150.0, 200,0.0, 300,_f, 0.22,_f,_f,_f,_f,_f,_f,_f,_f])
psspy.machine_data_2(503,r"""1""",[_i,_i,_i,_i,_i,_i],[ 0.0, 0.0, _f,_f,150,0.0, 166.7,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])
psspy.machine_data_2(550,r"""1""",[_i,_i,_i,_i,_i,_i],[ 0.0, 0.0, _f,_f,62,0.0, 62,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])
psspy.machine_data_2(550,r"""2""",[_i,_i,_i,_i,_i,_i],[ 0.0, 0.0, _f,_f,80,0.0, 80,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])
psspy.shunt_chng(507,r"""1""",_i,[_f, 100.0])
psspy.machine_chng_2(315,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])
#psspy.machine_chng_2(502,r"""5""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])
#psspy.machine_chng_2(550,r"""1""",[_i,_i,_i,_i,_i,_i],[ 50,_f,_f,_f,_f,0,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])
#psspy.machine_data_2(502,r"""5""",[1,_i,_i,_i,_i,_i],[ 200.0, 16.3377, 150.0,-150.0, 300.0,0.0, 333.33,_f, 0.22,_f,_f,_f,_f,_f,_f,_f,_f])
# #Bus 316 removing
# psspy.bsysinit(1)
# psspy.bsyso(1,316)
# psspy.extr(1,0,[0,0])
# #removed

powerflow=1 #powerflow=0 will enable dynamic simulation
nsm=5 #number of sync machines
Pload=1800
Qload=(251.32/2000)*Pload
Wload=400 #for 6 machines
Wchange=150 #assuming 100 added for each step of generator reduction

psspy.load_chng_5(315,r"""1""",[_i,_i,_i,_i,_i,_i,_i],[ -ic,119,_f,_f,_f,_f,_f,_f])
psspy.load_chng_5(504,r"""1""",[_i,_i,_i,_i,_i,_i,_i],[ (251.33/2000)*Pload,(33.51/251.32)*Qload,_f,_f,_f,_f,_f,_f])
psspy.load_chng_5(507,r"""1""",[_i,_i,_i,_i,_i,_i,_i],[(893.00/2000)*Pload,(108.91/251.32)*Qload,_f,_f,_f,_f,_f,_f])
psspy.load_chng_5(508,r"""1""",[_i,_i,_i,_i,_i,_i,_i],[(684.30/2000)*Pload,(83.77/251.32)*Qload,_f,_f,_f,_f,_f,_f])
psspy.load_chng_5(509,r"""1""",[_i,_i,_i,_i,_i,_i,_i],[(171.3670/2000)*Pload,(25.13/251.32)*Qload,_f,_f,_f,_f,_f,_f])
#psspy.branch_chng_3(506,507,r"""1""",[_i,_i,_i,_i,_i,_i],[0.0008*1.3,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],"")
psspy.branch_chng_3(507,509,r"""1""",[_i,_i,_i,_i,_i,_i],[0.016*1.4,0.06,0.2,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],"")
psspy.branch_chng_3(507,509,r"""2""",[_i,_i,_i,_i,_i,_i],[0.016*1.4,0.06,0.2,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],"")
if (nsm==6):
    x=Wload*0.7
    y=Wload*0.3
    psspy.machine_chng_2(503,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])
    psspy.two_winding_chng_5(503,506,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,502,_i,_i,0,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],"","")


if (nsm==5):
    x=(Wload+Wchange)*0.7
    y=(Wload+Wchange)*0.3
    psspy.machine_chng_2(503,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])
    psspy.machine_chng_2(502,r"""4""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])
    psspy.two_winding_chng_5(503,506,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,502,_i,_i,0,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],"","")
    psspy.two_winding_chng_5(502,505,r"""4""",[0,_i,_i,_i,_i,_i,_i,_i,502,_i,_i,0,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],"","")

if (nsm==4):
    x=(Wload+Wchange*2)*0.7
    y=(Wload+Wchange*2)*0.3
    psspy.machine_chng_2(503,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])
    psspy.machine_chng_2(502,r"""4""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])
    psspy.machine_chng_2(502,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])
    psspy.two_winding_chng_5(503,506,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,502,_i,_i,0,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],"","")
    psspy.two_winding_chng_5(502,505,r"""4""",[0,_i,_i,_i,_i,_i,_i,_i,502,_i,_i,0,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],"","")
    psspy.two_winding_chng_5(502,505,r"""3""",[0,_i,_i,_i,_i,_i,_i,_i,502,_i,_i,0,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],"","")
if (nsm==3):
    x=(Wload+Wchange*3)*0.7
    y=(Wload+Wchange*3)*0.3
    psspy.machine_chng_2(503,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])
    psspy.machine_chng_2(502,r"""4""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])
    psspy.machine_chng_2(502,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])
    psspy.machine_chng_2(502,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])
    psspy.two_winding_chng_5(503,506,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,502,_i,_i,0,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],"","")
    psspy.two_winding_chng_5(502,505,r"""4""",[0,_i,_i,_i,_i,_i,_i,_i,502,_i,_i,0,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],"","")
    psspy.two_winding_chng_5(502,505,r"""3""",[0,_i,_i,_i,_i,_i,_i,_i,502,_i,_i,0,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],"","")
    psspy.two_winding_chng_5(502,505,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,502,_i,_i,0,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],"","")

#psspy.machine_chng_2(502,r"""4""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])
#psspy.machine_chng_2(502,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])
#psspy.machine_chng_2(502,r"""3""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])
#psspy.machine_chng_2(503,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])
#psspy.machine_chng_2(503,r"""2""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])
#psspy.two_winding_chng_5(502,505,r"""2""",[0,_i,_i,_i,_i,_i,_i,_i,502,_i,_i,0,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],"","")
psspy.machine_chng_2(510,r"""1""",[_i,_i,_i,_i,_i,_i],[ x,_f, x*0.48,-x*0.48, x,_f, 1.11*x,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])
psspy.machine_chng_2(520,r"""1""",[_i,_i,_i,_i,_i,_i],[ y,_f,y*0.48,-y*0.48, y,_f, 1.11*y,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])
psspy.branch_chng_3(509,511,r"""1""",[_i,_i,_i,_i,_i,_i],[ (0.015/(0.01*x)),(0.025/(0.01*x)),_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],"")
psspy.branch_chng_3(508,521,r"""1""",[_i,_i,_i,_i,_i,_i],[ (0.015/(0.01*y)),(0.025/(0.01*y)),_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],"")
#psspy.branch_chng_3(507,511,r"""1""",[_i,_i,_i,_i,_i,_i],[ (0.015/(0.01*x)),(0.025/(0.01*x)),_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],"")
psspy.two_winding_chng_5(510,511,r"""1""",[_i,_i,_i,_i,_i,_i,_i,_i,510,_i,_i,0,_i,_i,_i],[0.0065/(0.01*x), (0.049/(0.01*x)),_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],"","")
psspy.two_winding_chng_5(520,521,r"""1""",[_i,_i,_i,_i,_i,_i,_i,_i,520,_i,_i,0,_i,_i,_i],[0.0065/(0.01*y), (0.049/(0.01*y)),_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],"","")


# psspy.purgmac(510,r"""1""")
# psspy.purgmac(520,r"""1""")
# psspy.load_data_5(510,r"""1""",[_i,_i,_i,_i,_i,_i,_i],[ -x,36.0,_f,_f,_f,_f,_f,_f])
# psspy.load_data_5(520,r"""1""",[_i,_i,_i,_i,_i,_i,_i],[ -y,29.0,_f,_f,_f,_f,_f,_f])
psspy.fnsl([0,0,0,1,1,1,99,0])


#e porjnto dll bananer age run kore nwa lage
if (powerflow==0):
	psspy.cong(0)
	psspy.conl(_i,_i,1,[0,_i],[_f,_f,_f,_f])
	psspy.conl(1,1,2,[_i,_i],[ 100.0,0.0,0.0, 100.0])
	psspy.conl(_i,_i,3,[_i,_i],[_f,_f,_f,_f])
	psspy.ordr(0)
	psspy.fact()
	psspy.tysl(0)
	psspy.dynamicsmode(0)
	if (proposed==1):
		psspy.dyre_new([1,1,1,1],r"""F:\PS project\shz\shz\qv_proposed.dyr""","","","")
	else:
		psspy.dyre_new([1,1,1,1],r"""F:\PS project\shz\qv_trivial.dyr""","","","")



    
    # psspy.plmod_status(502,r"""1""",7,0)
    # psspy.plmod_status(502,r"""2""",7,0)
    # psspy.plmod_status(502,r"""3""",7,0)
    # psspy.plmod_status(502,r"""4""",7,0)
    # psspy.plmod_status(502,r"""5""",7,0)
    # psspy.plmod_status(503,r"""1""",7,0)
    # psspy.plmod_status(503,r"""2""",7,0)
    # psspy.plmod_status(502,r"""4""",7,0)
    # psspy.plmod_status(503,r"""1""",7,0)
    # psspy.plmod_status(503,r"""1""",6,0)
    
	z=int(x/1.5)
	w=int(y/1.5) 
	psspy.change_wnmod_icon(510,r"""1""",r"""WT3G1""",1,z)
	psspy.change_wnmod_icon(520,r"""1""",r"""WT3G1""",1,w)
	

		
		
	psspy.dynamics_solution_param_2([250,_i,_i,_i,_i,_i,_i,_i],[ 0.3,_f, 0.002, 0.008,_f,_f,_f,_f])
	
	psspy.chsb(0,1,[-1,-1,-1,1,2,0])
	psspy.chsb(0,1,[-1,-1,-1,1,7,0])
	psspy.chsb(0,1,[-1,-1,-1,1,13,0])
	psspy.chsb(0,1,[-1,-1,-1,1,25,0])

    #    psspy.dist_branch_trip(315,509,r"""1""")
	psspy.strt_2([0,0],r"""F:\PS project\shz\qv.outx""")
	psspy.change_channel_out_file(r"""F:\PS project\shz\qv.outx""")
	psspy.run(0, 2.0,0,1,1)
	psspy.dist_branch_trip(315,509,r"""1""")
	psspy.run(0, 15,0,1,1)