# Gebou op iemand anders se bestaande tak

Soms wil of moet jy dalk bo-op die veranderinge aanbou wat 'n ander persoon reeds aan 'n tak van 'n lesbewaarplek toegewy het, bv. [as hulle nie meer die werk kan voltooi nie en jy wil help om hul trekversoek te voltooi] (/handbooks/maintainers.md#situation-1-a-pull-request-exists-but-is-incomplete).
Hierdie bladsy beskryf twee maniere waarop u kan opstel om bo-op te bou van die veranderinge wat hulle reeds aangebring het.
Die instruksies veronderstel 'n mate van vertroudheid met weergawebeheer, Git en GitHub.

## 1. Vurk hul bewaarplek en tak

### Vind die oorspronklike bydraer se vurk

Begin vanaf die oop trekversoek waaraan u wil voortgaan werk, blaai na die bokant van die oortjie _Gesprek_.
Onder die titel van die trekversoek vind u 'n opsomming van die takke wat gekombineer sou word as die trekversoek saamgesmelt is: gewoonlik die lesprogramorganisasie en `hoof` aan die linkerkant, en die oorspronklike bydraer se gebruikersnaam en die taknaam wat hulle aan die regterkant gekies het (die “kenmerktak”).

! [Takinligting vir 'n trekversoek op GitHub. Die naam van die amptelike standaardtak vir bewaarplek, `datacarpentry:main`, en van die bydraer se funksietak, `voorbeeld-gebruiker:voorbeeld-branch`, word vertoon.] (./img/branch-info-pr.png)

As u op die naam van die bydraer se funksietak klik, sal u na daardie tak op hul vurk van die lesbewaarplek lei.

### Maak jou eie vurk van hulle

Vanaf hierdie bladsy kan u u eie vurk van hul bewaarplek skep met die “Vurk” -knoppie regs bo van die bladsy.
Dit sal 'n kort vorm oopmaak waar u 'n naam en 'n beskrywing kan instel vir die nuwe vurk wat u sal skep.
Die belangrikste ding om hier te doen is **om die blokkie “Kopieer slegs die hooftak” -blokkie te verwyder** sodat u ook 'n afskrif van die funksietak kry waaraan hulle gewerk het vir die trekversoek.

! [Die vorm wat aangebied word wanneer 'n bestaande bewaarplek op GitHub gekies word, met die blokkie “Kopieer slegs die hooftak” ongekeerde.] (./img/new-fork-all-branches.png)

### Wysig die les op GitHub

Nadat u vurk geskep is, gebruik die aftreklys links bo van die bewaarplek tuisblad om die tak te kies waaraan die oorspronklike bydraer gewerk het.
Sodra hierdie tak gekies is, kan u die lêers op GitHub begin redigeer en versigtig wees om u veranderinge aan dieselfde tak toe te bring.
Alternatiewelik kan jy [die github.dev IDE in jou blaaier oopmaak] (https://docs.github.com/en/codespaces/the-githubdev-web-based-editor#opening-the-githubdev-editor), die tak kies en voortgaan om daar te redigeer en te doen.

### Wysig die les plaaslik

Volg hierdie stappe nadat u vurk geskep is.

1. Kloon dit na jou plaaslike stelsel.
2. Navigeer in die dop na u plaaslike kloon van die projek, bv. `cd ~/documents/datacarpentry/R-ecologie-leson`.
3. Kry die tak waaraan die oorspronklike bydraer gewerk het (`git fetch origin <their-branch-name>`, bv. `git fetch origin 123-better-captions`).
4. Skakel daaroor (`git switch <their-branch-name>`, bv. `git switch 123-better-captions`).

Sodra u aan hierdie tak gewerk het, kan u die les wysig en u veranderinge soos gewoonlik pleeg.
As jy gereed is, voeg jou eie vurk van die lesbewaarplek by as 'n afstandbestanddeel (`git remote add <remote-name> <address-of-forked-repository-you-just-copied>`, bv. `git remote add myfork git@github.com:myusername/image-processing.git`) druk die verbindings wat jy gemaak het en maak 'n trekversoek na die amptelike bewaarplek oop.

## 2. Voeg hul vurk by as 'n afgeleë bewaarplek

As u reeds 'n plaaslike kloon van die lesbewaarplek het, kan u die oorspronklike bydraer se vurk van die les voeg as 'n ander afgeleë bewaarplek vir die projek en die tak waaraan hulle gewerk het, van daar af haal.

1. Volg die stappe wat beskryf word in [_Vind die oorspronklike bydraer se vurk_] (#1-fork-their-repository-and-branch) hierbo.
2. Klik op die _Code_ -knoppie en kopieer die adres van hierdie bewaarplek na u knipbord.
3. Navigeer in die dop na u plaaslike kloon van die projek, bv. `cd ~/documents/datacarpentry/R-ecologie-leson`.
4. Voeg die oorspronklike bydraer se vurk by as 'n nuwe afstandbewaarplek vir hierdie kloon: `git remote add <remote-name> <address-of-forked-repository-you-just-copied>`,
   bv. `git remote add toby git@github.com:tobyhodges/image-processing.git`.
5. Haal die tak waaraan hulle gewerk het, van hul vurk, bv. `git fetch toby 123-better-captions`.
6. Skakel oor na hierdie tak, bv. `git switch 123-better-captions`.

Sodra jy aan hierdie tak gewerk het, kan jy die les wysig en jou veranderinge soos gewoonlik pleeg, dan dit na jou vurk druk en 'n trekversoek oopmaak wanneer jy gereed is.

## Maak 'n trekversoek oop met u opdaterings

As u gereed is om 'n nuwe trekversoek oop te maak wat u veranderinge sal insluit, maak seker dat u dit aan die regte bewaarplek doen (gewoonlik 'n bewaarplek in een van die Carpentries amptelike organisasies bv. `datacarpentry`): GitHub kan u eers help om 'n trekversoek na die oorspronklike bydraer se vurk oop in plaas van die sentrale Carpentries-bewaarplek.

Wanneer u u trekversoek oopmaak, vertel die Onderhouders dat u bo-op die vorige werk van die ander bydraer gebou het. Merk die oorspronklike bydraer en verwys na hul trekversoek volgens sy nommer, bv. “Hierdie trekversoek bou op en vervang #37 deur @USERNAME om uitgawe #34 te sluit deur ['n beskrywing van die veranderinge wat in jou trekversoek aangebring is...] '.
Dit sal die lesOnderhouders help om te verstaan dat hulle die ander trekversoek en die verhouding tussen die twee stelle veranderinge kan sluit.
