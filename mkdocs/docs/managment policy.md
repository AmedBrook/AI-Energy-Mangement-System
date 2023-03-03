Problem LP constraints
=====================

#### Linear programming constraints.

Linear programming constraints (LP constraints) are the rules that gouverne the problem optimization process. They are fondamentally set of equations, they might be either inequality equations ( example : ${a} + {b} \le {c}\hspace{0.3cm}$)   or equality equations  ( example : ${a} + {b} = {c}\hspace{0.3cm}$) constructed based on the LP variables quantities and problem parameters. (See. Problem LP variables and Problem LP constraints). 

#### Set of problem LP constraints.



- Load requirements:     $\hspace{2.5cm}L_k =P_k^{\mathrm{load}} +\eta {\;}^{\mathrm{fromBat}} {\cdot \;P}_k^{\mathrm{fromBat}}\hspace{2.1cm}$      $k=1,\dots ,n$  


- Power split:   $\hspace{3.9cm}P_{k\;} =P_k^{\mathrm{load}} {+\;P}_k^{\mathrm{toBat}}\hspace{4.5cm}$   $k=1,\dots ,n$


$\newline$ 

- Charge balance:  $\hspace{3.15cm}Q_k =Q_{k-1} +\eta^{\mathrm{toBat}} \cdot \;P_k^{\mathrm{toBat}} \Delta t-\;P_k^{\mathrm{fromBat}} \Delta t\hspace{0.3cm}$   

- Charge balance (initial):   $\hspace{1.8cm}Q_0 =Q_{\mathrm{init}}\hspace{4.3cm}$  



- Charge balance (final):     $\hspace{2cm}Q_n =Q_{\mathrm{final}}\hspace{6.3cm}$    $k=1,\dots ,n$

$\newline$ 

- Logical conditions on genset: $\hspace{0.8cm}P_{k\;} \le {0\ldotp 9P}_{\mathrm{max}\;} {\cdot y}_k\hspace{4.8cm}$    $k=1,\dots ,n$ 


- (0 or in 0.2P_max - 0.9Pmax):  $\hspace{0.8cm}P_{k\;} \le {0\ldotp 2P}_{\mathrm{max}\;} {\cdot y}_k\hspace{4.7cm}$    $k=1,\dots ,n$


$\newline$ 

- Logical conditions on battery:   $\hspace{0.8cm}y_k^{\mathrm{toBat}} +y_{k\;}^{\mathrm{fromBat}} \le 1\hspace{4.3cm}$     $k=1,\dots ,n$  
$\newline$     
$\hspace{6.2cm}P_k^{\mathrm{toBat}} \le 0\ldotp 9P_{\mathrm{max}} {\cdot y}_k^{\mathrm{toBat}}\hspace{3.7cm}$ $k=1,\dots ,n$ 


$\hspace{6.9cm}P_k^{\mathrm{fromBat}} \le 0\ldotp 9P_{\mathrm{max}} {\cdot \;y}_k^{\mathrm{fromBat}}\hspace{2.6cm}$  $k=1,\dots ,n$ 


$\newline$ 

- Constraints for linearization of objective:  $\hspace{0.5cm}z_k \ge y_k -y_{k-1}\hspace{3.6cm}$ $k=2,\dots ,n$
