Simple recursive descent parser for Blaise like languages.<br><br>

Multimode Interviewing Capability (MMIC) - RAND Corporation<br>
Nubis - USC CESR<br>
Blaise - Statistics Netherlands<br>
<br>

Example Nubis.bla<br>

<pre>

// FOR FAM R
FLHC002.FILL
HC001[HCcnt]-
HC006
HC002
FOR HCcnt := 1 TO 10 DO
 IF HCcnt IN HC002 THEN
   HC003[HCcnt]-
   IF HC006 = 1 THEN
     IF HCcnt != 8 THEN  // dont ask for food eat...
       HC004[HCcnt] := 2
       IF HC004[HCcnt]  = 1 THEN
         HC005[HCcnt]
       ENDIF
     ENDIF
   ENDIF
 ENDIF
ENDDO
HC003
IF HC003 = 1 THEN
    HC004
ELSEIF HC004 = 2 THEN
    HC003
ELSEIF HC005 = 3 THEN
    HC006
ELSE
    HC005
ENDIF
HDD := 3 + 2 * 1 + 2


</pre>

Parse tree output:

<pre>
(MethodCall FLHC002 FILL)
 (ArrayAccess HC001 HCcnt)
 ASK Identifier: HC006 
 ASK Identifier: HC002 
 FOR Identifier: HCcnt   :=  1 TO 10  DO
				IF ExpressionNode: (IN HCcnt HC002)  THEN
								(ArrayAccess HC003 HCcnt)
								IF ExpressionNode: (= HC006 1)  THEN
												IF ExpressionNode: (!= HCcnt 8)  THEN
																(:= (ArrayAccess HC004 HCcnt) 2)
																IF ExpressionNode: (= (ArrayAccess HC004 HCcnt) 1)  THEN
																				(ArrayAccess HC005 HCcnt)
 ASK Identifier: HC003 
 IF ExpressionNode: (= HC003 1)  THEN
				ASK Identifier: HC004 
 ELSE
				IF ExpressionNode: (= HC004 2)  THEN
								ASK Identifier: HC003 
				ELSE
								IF ExpressionNode: (= HC005 3)  THEN
												ASK Identifier: HC006 
								ELSE
												ASK Identifier: HC005 
 (:= HDD (+ (+ 3 (* 2 1)) 2))

</pre>
