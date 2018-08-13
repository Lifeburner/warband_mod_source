## Prebattle Orders & Deployment by Caba'drin
## v0.92.5
## 30 March 2012


info_pages = [
##PBOD
("prebattle", "Pre-Battle Planning", "A tactics-savvy commander has more options open to {him/her}self when going to battle. Rather than simply charging in, {he/she} can choose to Lead {his/her} troops into battle (all begin following) or to simply Take the Field (all begin holding).^^Those with more tactical training can create advanced pre-battle plans, giving a series of complex orders to each divisional captain to execute when the battle begins. These trained commanders can also tell their captains which troops should attack in the first wave and thus choose which troops will deploy at the battle's beginning and which troops should serve as reinforcements. These plans will be remembered between battles, but the relevant orders will need to be dispatched to the divisional captains before each battle.^^It is at times useful to divide one's party into divisons beyond the standard three of infantry, archers, and cavalry. When examining the Party, different types of soldiers can be assigned to additional groups and those groups given names. Additionally, in consultation with one's captains in Camp, troops of the same type can be split into secondary divisions so that a good commander might have two divisions of heavy cavalry or infantry for flanking maneuvers. Such assignments will be active across many battles, until the troop captains are instructed otherwise."),
("tactics", "Tactics", "While in-battle, an effective commander gives the troops under {him/her} clear orders to help lead them to victory. As war in the Holy Land continues to toil on, more advanced orders and tactics have been developed and are now more widely used by field commanders. For instance, on the basic end, a commander can order {his/her} troop divisions to use specific weapon types (one handed, two handed, polearms, or ranged) as well as whether or not to wield their shields, rather than leave these decisions up to the individual troops. (Also, unless noted otherwise--in Mod Options--troops' decision making about weapon use has improved for all polearm infantry, lance-wielding cavalry, and mounted archers. These troops have been instructed to use their polearms, lances, and horsebows unless they are separated and surrounded by enemies.)^^Troop divisions can also create cohesive formations, improving their fighting force as a unit and staying more organized in the heat of battle. Infantry are allowed the widest variety of divisions, forming a battle square, a three-rank formation with the strongest units in the front ranks, a three-ranked shield wall with the stoutest shield-users to the front, and a wedge to break through enemy formations and led by the strongest troops. Cavalry divisions can only form this wedge, while foot archers can only form up in ranks. (If you, the player, allow it--in Mod Options--enemy forces can use these formations as well, either with the Native AI or with completely reworked Formations AI.)^^Commanders in the Holy Land have also developed more advanced tactical responses to their enemies. These attack and special orders are useful for a sharp commander in countering specific threats or pressing {his/her} own tactical advantage. For instance, ranged troops can be instructed to skirmish and avoid direct melee contact with the enemy by running away until they re-establish adequate distance. Archers and crossbowmen can be ordered to fire in volleys, rather than at will, syncronizing their flights of missiles and effectively slowing an enemy advance. A useful tactic for polearm infantry is to brace the butts of their spears and pikes into the ground and against the inside of their feet in preparation to receive a cavalry charge. A smart cavalry commander will avoid ranks of pikes braced to receive and destroy their horses. (If you, the player, allow it--in Mod Options--enemy forces can use these advanced 'special' orders as well.)^^Beyond the added control of telling divisions how to conduct themselves to best effect, commanders also have the ability to direct {his/her} divisions in targetting specific enemy divisions, so cavalry can counter a cavalry charge or whipe out pesky archers and heavy infantry can clear enemy pokearms in advance of a cavalry charge. To do this, a commander should make use of {his/her} field flags (the hold-down-F1 flag) and drop them on the enemy division; {his/her} listening divisions will move to attack the specified target.^^If a commander falls in battle, {his/her} troops can carry on fighting once {his/her} personage is secured for recovery after the battle. A commander must specify (in Mod Options) if {his/her} troops should continue fighting under their previous orders, charge in an attempt to prevent the tide of battle from swinging against them, or have the division captains take command and conduct the battle as they see fit (battle continuation formations AI is only available if also activated for the enemy AI team).^^The above weapon-type and formations orders, as well as some of the more advanced tactical maneuvers/attack orders can be outlined as part of a commander's pre-battle plans.^^For a smart commander, tactical thinking does not end on the battlefield. Not only does {he/she} make pre-battle plans, but {he/she} takes care when travelling into towns and villages to gather supplies, bringing close companions as escort. In order to convince companions to serve in this capacity and to not appear foolish, the number of bodyguards a commander uses is based on {his/her} leadership and renown."),
##PBOD
]

from util_common import add_objects

# Used by modmerger framework version >= 200 to merge stuff
# This function will be looked for and called by modmerger if this mod is active
# Do not rename the function, though you can insert your own merging calls where indicated
def modmerge(var_set):
    try:
        var_name_1 = "info_pages"
        orig_info_pages = var_set[var_name_1]
        add_objects(orig_info_pages, info_pages)
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)