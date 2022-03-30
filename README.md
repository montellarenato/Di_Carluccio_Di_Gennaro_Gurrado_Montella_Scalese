# Advance Ruzzle and Letters Labyrinth
# A.R.A.L.L.
  

Autori-programmatori: Di Carluccio, Di Gennaro, Gurrado, Montella, Scalese.
Scuola: Gian Battista Vico 
Classe: 4°   Sez: E
Anno: 2021/2022




Descrizione gioco        
 REGOLE GIOCO        
 REGOLE PER IL CALCOLO DEL PUNTEGGIO        
 FUNZIONAMENTO        
  INTERFACCIA DI LOGIN        
  INTERFACCIA DEL GIOCO        
  COLLEGAMENTO ALLA TEORIA        
  SALVATAGGIO DATI                
Richiami matematici        
 PERMUTAZIONI        
 DISPOSIZIONI        
 COMBINAZIONI        
 PROBABILITÀ        

## Descrizione gioco
Il gioco creato è A.R.A.L.L (Advance Ruzzle and Letters Labyrinth).
Il nome del gioco è formato dall'acronimo delle iniziali dei nomi degli autori del gioco (A)ntonio(R)enato(A)ndrea(L)uca(L)orenzo.
Lo scopo del gioco è quello di trovare il maggior numero di parole possibili, così da raggiungere il punteggio maggiore.
### REGOLE GIOCO
Il gioco A.R.A.L.L. è basato su poche e semplici regole. Le parole possono essere formate da qualsiasi tipo di combinazione tra lettere prese una singola volta, in caso contrario non si riceverà nessun punto. Il gioco presenta due modalità: “giocatore singolo” o “più giocatori”.  Per entrambe le modalità sono presenti le parole bonus, ovvero parole di una determinata categoria che viene sorteggiata casualmente prima dell’inizio del tempo, ed il tempo stabilito è di 1 minuto per round:
* Giocatore singolo: per arrivare alla vittoria bisogna superare la soglia del punteggio-minimo del livello prestabilita una volta avviato quest’ultimo, per avanzare a quello successivo. In questa modalità ci sono 3 difficoltà:
   * principiante: non bisogna trovare le parole bonus;
   * intermedio: bisogna trovare un minimo di 3 parole bonus;
   * difficile: bisogna trovare un minimo di 6 parole bonus.
* Più giocatori: per arrivare alla vittoria bisogna trovare quante più parole possibili prima che si esaurisca il tempo con l’obiettivo di superare il punteggio degli avversari.
### REGOLE PER IL CALCOLO DEL PUNTEGGIO
Il punteggio aumenta in base a determinate regole: 
* la lunghezza della parola ne determina il punteggio:
   * dalle 2 alle 4 lettere = 2 punti
   * dalle 5 alle 8 = 5 punti
   * 9 lettere = 10 punti
* Le parole bonus valgono doppio.
* Una serie di 5 parole giuste concede un bonus di 5 punti alla fine del livello.
### FUNZIONAMENTO
Il gioco è stato sviluppato con il software Python, che utilizza il linguaggio di programmazione C. Grazie ad esso è stato possibile realizzare la classe calcolo combinatorio, che funge da base per il funzionamento del gioco, e per l’idealizzazione della parte grafica. Quest’ultima si suddivide in due interfacce che, facendo riferimento al diagramma allegato, corrispondono rispettivamente al blocco “inizializzazione 1” e “inizializzazione 2”.
Per inizializzazione si intende un blocco contenente varie funzioni. Nel gioco sono presenti due tipi di inizializzazioni, le quali svolgono compiti diversi:
* inizializzazione 1: consiste nella comparsa della schermata principale dove è possibile registrarsi o accedere al proprio account.
* inizializzazione 2: consiste nel passaggio dalla schermata principale alla schermata di gioco, creazione dell’interfaccia e generazione delle parole.
#### INTERFACCIA DI LOGIN
Il blocco “inizializzazione 1” consiste nella generazione dell’interfaccia di login, ovvero di una sezione in cui, prima di iniziare a giocare vi è l’obbligo di creare un proprio account o di effettuare il login in un account già esistente.
L’interfaccia di login è costituita da:
* una sezione in cui inserire il proprio username
* una sezione in cui inserire la propria password
* una sezione in cui compare la scritta “accedi” nel caso in cui si effettua il login
* una sezione in cui compare la scritta “iscriviti” nel caso in cui non si abbia già un account
#### INTERFACCIA DEL GIOCO  
Il blocco “inizializzazione 2” del diagramma corrisponde alla generazione dell’interfaccia di gioco, costituita da:
* una griglia 3x3 in cui vengono generate le lettere.
* una sezione situata in alto a sinistra in cui compare il tempo di gioco rimanente.
* una tabella di testo in cui vengono inserite le parole trovate dal giocatore.
* una sezione situata sul centro-destra in cui, attraverso l’uso di una spunta verde o una croce rossa, si indica se la parola inserita dal giocatore è giusta o sbagliata.
* una sezione situata in alto a destra in cui viene indicato il punteggio del giocatore.
* una sezione situata in alto al centro in cui compare la scritta “exit”, che permette al giocatore di terminare la partita e uscire dal gioco.
* una sezione situata in basso a destra in cui compare la scritta “next”, che permette al giocatore di avanzare al livello successivo. 
#### COLLEGAMENTO ALLA TEORIA
Bisogna specificare due aspetti fondamentali, cioè in che modo la teoria cioè le regole del calcolo combinatorio sono servite per la realizzazione del gioco. La generazione delle lettere all’ interno della tabella segue le regole delle permutazioni, disposizioni e disposizioni. Inoltre la generazione delle lettere deve considerare il calcolo della probabilità del calcolo combinatorio, perché nel caso contrario uno dei due giocatori verrebbe svantaggiato. In questo gioco la probabilità viene calcolata in base alle parole che si possono formare con quelle determinate lettere, così da dare la stessa possibilità di punteggio massimo ad entrambi i giocatori
#### SALVATAGGIO DATI
Il primo salvataggio che avviene è quello degli account creati, i quali vengono memorizzati e salvati nella funzione “salva account” Nella funzione, sempre presente nel diagramma,  “salvataggio dati” il gioco dà la possibilità di salvare il proprio punteggio nella partita corrente, e dà anche la possibilità di salvare le statistiche legate al proprio account, come ad esempio le partite giocate, i punti totali, le vittorie in multigiocatore e il livello raggiunto in giocatore singolo. Nel caso della sezione multigiocatore si utilizza contemporaneamente un altro tipo di salvataggio, in remoto, che salva i dati della singola partita del giocatore in modo da essere confrontati nella funzione “confronta i punteggi”, e con la funzione “decreta il vincitore”, si saprà chi ha vinto . 

## Richiami matematici
### PERMUTAZIONI
Una permutazione è il risultato di uno scambio dell'ordine degli elementi di una sequenza, ossia è uno dei possibili modi per ordinare elementi di qualsiasi tipo. Si distinguono due tipi di permutazioni: le permutazioni semplici, le permutazioni con ripetizione.
* Permutazioni semplici: le permutazioni semplici di n elementi distinti sono tutti i gruppi formati dagli n elementi, che differiscono per il loro ordine Pn = n!
* Permutazioni con ripetizioni: Le permutazioni con ripetizioni di n elementi di cui h, k,... ripetuti, sono tutti i gruppi formati  dagli n elementi, che differiscono per l’ordine in cui si presentano gli elementi distinti e la posizione che occupano gli elementi ripetuti. Pn(h,k…) = n! /  h! * k! *…


### DISPOSIZIONI
Come per le permutazioni anche le disposizioni sono con e senza ripetizioni:
* DIsposizioni semplici: Le disposizioni semplici di n elementi distinti di classe k (con n,k appartenenti a N e k≤n) sono tutti i gruppi che si possono formare con k elementi, presi fra gli n, tali che ognuno è diverso dagli altri per gli elementi contenuti o l’ordine. Dn,k= n* (n-1) * (n-2)*...*(n-k+1)=n!/(n-k)!
* Disposizioni con ripetizioni: Le disposizioni con ripetizioni di n elementi distinti di classe k( con n,k appartenenti a N) sono tutti i gruppi che si possono formare con k elementi, anche ripetuti, presi fra gli n, tali che ogni gruppo è diverso dagli altri per gli elementi contenuti o per il loro ordine. D’n,k = nk


### COMBINAZIONI
Una combinazione è un raggruppamento di k elementi, presi in qualsiasi ordine, formato a partire da n elementi distinti. In termini più rigorosi si dice combinazione ogni sequenza di k elementi estratti tra  n elementi distinti, nell'ipotesi che l'ordine di estrazione sia ininfluente. Pure in questi caso esistono combinazioni semplici e con ripetizioni:
* Combinazioni semplici: Le combinazioni semplici di n elementi distinti di classe k (con 0<k≤n) sono tutti i gruppi che si possono formare con k elementi, presi fra gli n, e tali che ogni gruppo è diverso dagli altri per almeno un elemento contenuto. Cn,k=Dn,k/ Pk=n!/k!(n-k)!
* Combinazioni con ripetizioni:  Le combinazioni con ripetizioni di n elementi distinti di classe k, sono tutti i gruppi che si possono formare con k elementi, presi fra gli n; ogni elemento di un gruppo può essere ripetuto fino a k volte, non interessa l’ordine in cui gli elementi si presentano e in ciascun gruppo è diverso il numero delle volte in cui un elemento compare. C’n,k=Cn+k-1,k=(n+k-1)*(n+k-2)*.../k!


### PROBABILITÀ
La probabilità di un evento (E) è il rapporto fra il numero dei casi favorevoli (f) e quello dei casi possibili (u) quando sono tutti ugualmente possibili. p(E)= f/u.
Poiché il numero dei casi favorevoli è sempre minore o uguale al numero dei casi possibili la probabilità di evento è sempre compresa tra 0 e 1.  0 ≤ p(E ) ≤ 1
Poi abbiamo dei casi particolari:
* Quando il numero dei casi favorevoli è uguale al numero dei casi possibili l’evento sarà certo cioè uguale a 1. p(E)=1
* Quando il numero dei casi favorevoli è uguale a 0 cioè nullo l’evento sarà impossibile. p(E)=0
