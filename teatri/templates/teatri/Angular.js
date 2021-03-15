var sito=angular.module('myApp', [])

//cambio tema
sito.controller('Tema', function($scope) {
    $scope.count = 0;
	$scope.val = 0;
    $scope.tema = 'text-black bg-light';
    $scope.myFunction = function() {
        $scope.count++;
        if ($scope.count%2==0) {
            $scope.tema="text-black bg-light";
        }else{
            $scope.tema="text-white bg-dark";
        }
    }
});
//INDEX
//reindirizzamento pagine
sito.controller('vociMenu', ['$scope', function ($scope) {
$scope.Immagini = [
	{nome:"Fig. 1: sezioni profilo Instagram", link:"#FIG1", url:"Fig1.png"},
	{nome:"Fig. 2: esempi di fotografia  casual, professional e designed",link:"#FIG2", url:"Fig2.png"},
	{nome:"Fig. 3: esempio di varietà di contenuti profilo teatro",link:"#FIG3", url:"Fig3.png"},
	{nome:"Fig. 4: profilo progetto collegato a profilo teatro",link:"#FIG4", url:"Fig4.png"},
    {nome:"Fig. 5: post di un profilo informativo",link:"#FIG5", url:"Fig5.png"},
    {nome:"Fig. 6: una foto professional da campione profili teatro",link:"#FIG6", url:"Fig6.png"},
    {nome:"Fig. 7: una foto casual da campione profili progetto",link:"#FIG7", url:"Fig7.png"},
    {nome:"Fig. 8: una foto designed da campione profili informativi",link:"#FIG8", url:"Fig8.png"}
        ];
$scope.Tabelle = [
	{nome:"Tab. 1: analisi generale con NLTK", link:"#TAB1"},
	{nome:"Tab. 2: frequenze parole particolari",link:"#TAB2"},
	{nome:"Tab. 3: analisi generale con DyLan",link:"#TAB3"},
	{nome:"Tab. 4: analisi lessicale espressa in percentuali con DyLan",link:"#TAB4"},
    {nome:"Tab. 5: analisi sintattica espressa in percentuali con DyLan",link:"#TAB5"},
    {nome:"Tab. 6: analisi tag e hashtag",link:"#TAB6"},
    {nome:"Tab. 7: frequenze tag e hashtag",link:"#TAB7", url:"Tab7.png"},
    {nome:"Tab. 8: caratteristiche foto profili teatro",link:"#TAB8"},
    {nome:"Tab. 9: valori categorie e caratteristiche foto profili",link:"#TAB9"}
        ];
        
}]);

//gestione link INDEX
sito.controller('OpenWin', ['$compile', '$scope','$window', function($compile, $scope, $window) {
  $scope.Click = function(pagina) {
      $window.open(pagina, "_self");
};}]);





