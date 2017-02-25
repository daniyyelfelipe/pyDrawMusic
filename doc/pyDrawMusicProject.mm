<map version="freeplane 1.5.9">
<!--To view this file, download free mind mapping software Freeplane from http://freeplane.sourceforge.net -->
<node TEXT="pyDrawMusic" FOLDED="false" ID="ID_1270955882" CREATED="1487081219096" MODIFIED="1487081453886" STYLE="oval">
<font SIZE="18"/>
<hook NAME="MapStyle" background="#ffffcc">
    <properties fit_to_viewport="false;"/>

<map_styles>
<stylenode LOCALIZED_TEXT="styles.root_node" STYLE="oval" UNIFORM_SHAPE="true" VGAP_QUANTITY="24.0 pt">
<font SIZE="24"/>
<stylenode LOCALIZED_TEXT="styles.predefined" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="default" COLOR="#000000" STYLE="fork">
<font NAME="SansSerif" SIZE="10" BOLD="false" ITALIC="false"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.details"/>
<stylenode LOCALIZED_TEXT="defaultstyle.attributes">
<font SIZE="9"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.note" COLOR="#000000" BACKGROUND_COLOR="#ffffff" TEXT_ALIGN="LEFT"/>
<stylenode LOCALIZED_TEXT="defaultstyle.floating">
<edge STYLE="hide_edge"/>
<cloud COLOR="#f0f0f0" SHAPE="ROUND_RECT"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.user-defined" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="styles.topic" COLOR="#18898b" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subtopic" COLOR="#cc3300" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subsubtopic" COLOR="#669900">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.important">
<icon BUILTIN="yes"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.AutomaticLayout" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="AutomaticLayout.level.root" COLOR="#000000" STYLE="oval" SHAPE_HORIZONTAL_MARGIN="10.0 pt" SHAPE_VERTICAL_MARGIN="10.0 pt">
<font SIZE="18"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,1" COLOR="#0033ff">
<font SIZE="16"/>
<edge COLOR="#ff0000"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,2" COLOR="#00b439">
<font SIZE="14"/>
<edge COLOR="#0000ff"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,3" COLOR="#990000">
<font SIZE="12"/>
<edge COLOR="#00ff00"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,4" COLOR="#111111">
<font SIZE="10"/>
<edge COLOR="#ff00ff"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,5">
<edge COLOR="#00ffff"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,6">
<edge COLOR="#7c0000"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,7">
<edge COLOR="#00007c"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,8">
<edge COLOR="#007c00"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,9">
<edge COLOR="#7c007c"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,10">
<edge COLOR="#007c7c"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,11">
<edge COLOR="#7c7c00"/>
</stylenode>
</stylenode>
</stylenode>
</map_styles>
</hook>
<hook NAME="AutomaticEdgeColor" COUNTER="4" RULE="ON_BRANCH_CREATION"/>
<hook NAME="accessories/plugins/AutomaticLayout.properties" VALUE="ALL"/>
<node TEXT="Definition" POSITION="right" ID="ID_1573168564" CREATED="1487081271638" MODIFIED="1487081275657">
<edge COLOR="#ff0000"/>
<node TEXT="A computer software writed in python language that uses the turtle library to draw musical elements." ID="ID_335150078" CREATED="1487081305483" MODIFIED="1487081353454"/>
</node>
<node TEXT="Program folder and files structure" POSITION="right" ID="ID_1294552453" CREATED="1487081405141" MODIFIED="1487081499485" HGAP_QUANTITY="14.749999977648258 pt" VSHIFT_QUANTITY="17.249999485909953 pt">
<edge COLOR="#ff00ff"/>
<node TEXT="pyDrawMusic.py" ID="ID_563117866" CREATED="1487081501680" MODIFIED="1487081635651" LINK="../pyDrawMusic.py"/>
<node TEXT="doc" ID="ID_1288477460" CREATED="1487081511819" MODIFIED="1487081514177">
<node TEXT="pyDrawMusicProject.mm" ID="ID_1451850211" CREATED="1487081531956" MODIFIED="1487081648177" LINK="pyDrawMusicProject.mm"/>
</node>
<node TEXT="lib" ID="ID_768793158" CREATED="1487081514687" MODIFIED="1487081515987">
<node TEXT="__init__.py" ID="ID_1754784630" CREATED="1487081544529" MODIFIED="1487081625838" LINK="../lib/__init__.py"/>
<node TEXT="turtlePaterns.py" ID="ID_1018508597" CREATED="1487081556260" MODIFIED="1487081619932" LINK="../lib/turtlePaterns.py"/>
</node>
</node>
<node TEXT="Concepts" POSITION="right" ID="ID_1220945684" CREATED="1487081284702" MODIFIED="1487081453882" HGAP_QUANTITY="17.749999888241295 pt" VSHIFT_QUANTITY="14.999999552965178 pt">
<edge COLOR="#00ff00"/>
<node TEXT="Musical elements" ID="ID_118486068" CREATED="1487081688795" MODIFIED="1487081707465">
<node TEXT="note" ID="ID_1339558969" CREATED="1487081715616" MODIFIED="1487081794413">
<node TEXT="wikpedia" ID="ID_1126103665" CREATED="1487082209979" MODIFIED="1487082240302" LINK="https://en.wikipedia.org/wiki/Musical_note"/>
</node>
<node TEXT="rest" ID="ID_86761896" CREATED="1487081723146" MODIFIED="1487081791088">
<node TEXT="wikpedia" ID="ID_838182228" CREATED="1487082295487" MODIFIED="1487082301436" LINK="https://en.wikipedia.org/wiki/Rest_(music)"/>
</node>
<node TEXT="pentagrama" ID="ID_1700412453" CREATED="1487081735990" MODIFIED="1487082013248"/>
<node TEXT="bar" ID="ID_637513142" CREATED="1487081747417" MODIFIED="1487081754699"/>
<node TEXT="clef" ID="ID_553659422" CREATED="1487081759872" MODIFIED="1487081761863"/>
<node TEXT="formula de compasso" ID="ID_81632427" CREATED="1487081831954" MODIFIED="1487081893568"/>
<node TEXT="armadura da clave" ID="ID_166491513" CREATED="1487081974348" MODIFIED="1487082004882"/>
<node TEXT="score" ID="ID_633887788" CREATED="1487082374909" MODIFIED="1487082377210">
<node TEXT="wikpedia" ID="ID_1552681871" CREATED="1487082383628" MODIFIED="1487082389658" LINK="https://en.wikipedia.org/wiki/Musical_score"/>
</node>
<node TEXT="notation" ID="ID_540182529" CREATED="1487082484114" MODIFIED="1487082486107">
<node TEXT="wikpedia" ID="ID_1190058222" CREATED="1487082487352" MODIFIED="1487082492772" LINK="https://en.wikipedia.org/wiki/Musical_notation"/>
</node>
</node>
</node>
</node>
</map>
