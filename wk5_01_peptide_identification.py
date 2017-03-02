"""
Solution to the Peptide Identification Problem.
Molecular Evolution (Bioinformatics IV) on Coursera.org
Week 5, code challenge #1
"""

import constants as co


def peptide_identification(vector,proteome):
    '''
    Peptide Identification Problem.
    
    Parameters
    --------
    vector: space-delimited spectral vector Spectrum (string or list of integers)
    proteome: amino acid string Proteome (string)
    
    Return
    --------
    Substring of proteome with the highest match against the given spectrum. (string)
    '''
    def convert_input(input_data):
        '''
        Converts input for peptide_identification.
        '''
        split_data = input_data.split()
        vector = []
        for e in split_data:
            vector.append(int(e))
        return vector
    
    def calculate_score(peptide):
        score = 0
        vector_index = -1
        for amino_acid in peptide:
            
            new_index = vector_index + co.masses_integers[amino_acid]
            if new_index < len(vector):
                score += vector[new_index] 
            vector_index = new_index
        if vector_index != len(vector) - 1:
            score = 0
        return score
    
    if type(vector) == str:
        vector = convert_input(vector)   
        
    # calculate the minimum and maximum length the peptide could be 
    # reversed masses is a dict with masses as keys and AAs as values
    max_peptide_len = len(vector)/min(co.reversed_masses.keys()) # length of peptide composed solely of the amino acid with the smallest mass
    min_peptide_len = len(vector)/max(co.reversed_masses.keys()) # length of peptide composed solely of the amino acid with the largest mass
    
    max_score = float('-inf')
    max_seq = ''
    
    # calculate the score for all peptides with lengths between the min and max peptide lengths
    for i in range(min_peptide_len,max_peptide_len+1):
        for j in range(0,len(proteome) - i):
            peptide_score = calculate_score(proteome[j:j+i])
            
            # if the current peptide score is greater than the max score, set the current peptide as the highest scoring peptide
            if peptide_score > max_score:
                max_score = peptide_score
                max_seq = proteome[j:j+i]

    return max_seq, max_score
    

###############################################################
if __name__ == "__main__":
    challenge_data_vector = '25 -2 17 -6 21 -7 25 13 9 -4 -5 11 6 4 6 -1 28 -10 5 8 -3 -19 -14 -3 20 -12 19 20 27 23 -4 -14 5 -16 -8 -3 -9 -17 18 14 11 27 -11 16 3 26 10 -8 -13 22 -8 -5 -17 -20 -14 1 21 -10 7 28 26 17 -20 16 8 5 2 -16 -17 21 -17 -11 19 24 7 -6 11 6 -4 18 -2 -11 18 -13 26 -19 -18 12 -19 12 -4 4 8 23 27 19 -18 30 -17 -6 8 11 0 10 -10 4 -20 6 -9 7 14 -17 19 10 19 -8 20 19 24 -7 24 2 23 10 6 30 -18 3 20 -12 30 28 12 -4 18 5 -2 7 12 -13 -6 4 -4 -3 -12 -9 -4 7 23 30 15 11 -1 30 2 -9 15 26 18 14 15 23 -15 1 -1 18 -3 -12 -13 5 27 27 14 -12 2 -15 30 -4 14 -4 8 -9 7 11 29 10 -5 11 2 27 -10 12 23 17 -16 27 30 21 24 21 -9 2 25 -18 6 3 6 -17 7 11 -17 -1 22 13 8 -19 -5 -1 -8 30 3 8 -18 -14 16 -11 9 29 24 0 -5 30 29 -9 -9 25 16 -12 26 -15 21 -5 14 0 -9 -6 -18 18 -20 20 17 0 -6 4 11 10 4 -5 -9 8 -11 -16 16 -1 4 12 -14 -15 -13 -11 -4 5 22 7 12 29 25 2 8 23 1 24 -20 25 24 12 6 24 22 22 -5 19 17 29 11 2 12 -5 -1 13 11 17 4 12 19 -11 -3 8 -12 19 19 -13 0 10 -14 26 -16 2 30 -6 -3 5 20 8 8 17 -17 9 -4 12 -2 19 10 -4 -1 -10 12 3 7 17 1 5 -4 14 17 18 19 29 -20 27 -16 0 11 0 3 -9 0 25 -14 8 15 -2 26 6 -7 0 24 9 -12 27 17 1 -2 19 15 11 9 -2 28 10 -12 -16 -7 24 -2 7 16 3 12 -1 -11 28 -10 21 -18 -5 18 22 0 26 27 -7 -18 -9 22 5 -14 28 17 6 12 -7 26 12 -11 16 -12 3 -16 29 20 30 20 -16 -6 -3 -18 -9 -16 27 -20 5 -2 25 29 -4 28 28 12 -8 -3 -17 6 -1 -6 10 -16 16 1 -1 9 18 16 0 11 27 26 13 29 -8 16 -11 14 -12 14 0 -17 25 -6 21 15 29 15 2 6 18 -18 -3 21 -15 19 -11 3 4 7 10 17 27 24 28 16 3 25 -14 8 17 -17 -5 0 21 -17 -18 -11 6 9 -5 11 14 -10 27 -18 26 -18 26 -11 -20 25 -18 15 -20 -1 24 -4 -11 12 7 -5 -2 -12 26 -5 -15 20 22 3 -5 15 -7 25 23 -17 -5 28 23 28 6 13 10 -4 6 27 8 14 22 -2 9 14 12 -17 21 29 -18 14 -9 -9 -8 -8 -15 2 26 4 0 12 5 18 10 17 23 -1 24 4 19 -1 26 1 11 18 14 21 -4 24 7 6 -7 11 24 26 -10 -7 -4 14 15 4 27 15 -8 -15 27 17 13 -9 3 20 -4 19 -13 0 -6 2 19 15 -20 29 3 -19 14 7 -5 -6 -17 7 -14 28 25 22 -14 18 -3 -20 -16 -16 -17 25 5 16 -17 -4 0 9 15 9 -9 14 11 0 30 19 30 -7 -3 -13 -20 0 -17 20 5 12 -20 14 30 -5 0 18 11 0 4 2 -13 7 11 -11 5 17 12 11 27 12 23 4 30 -6 7 5 15 9 -2 11 22 0 26 11 -20 23 -10 -5 28 -4 28 -20 -3 5 17 17 5 -12 22 26 -12 13 28 -7 18 2 25 6 16 23 25 -12 -4 29 28 21 9 -8 -14 10 -13 -18 22 -6 -1 -2 19 -18 -9 26 -16 16 -19 10 -5 -19 -4 26 -20 0 6 -9 4 30 -3 10 26 9 -1 15 26 -17 4 20 -16 -4 9 -12 -8 21 1 27 -7 11 11 28 5 25 -9 -10 30 12 24 -2 -16 23 4 -4 8 23 -14 -15 -17 21 22 9 14 -4 -18 -13 -8 18 28 -9 23 20 15 -16 -3 -9 12 -3 22 -2 18 22 7 -19 -11 22 27 -20 15 20 0 19 19 18 25 -8 1 27 2 -1 19 9 0 -16 2 -8 11 -1 0 -16 -14 13 0 21 24 3 26 30 12 -20 30 18 8 14 16 -1 -1 17 26 15 -19 -2 19 -15 -10 -12 2 11 3 15 17 10 -3 29 15 -18 20 2 2 5 -17 -8 15 -13 -18 -14 20 16 -2 -16 5 15 -7 12 -14 -18 -4 4 -11 -3 7 -14 26 -17 -11 15 -17 -17 -11 28 -17 -4 21 22 20 15 20 -7 8 14 -20 25 7 6 21 25 -19 15 14 22 -12 -5 0 -1 23 2 1 10 30 8 21 26 27 -14 22 -1 7 26 3 2 7 27 26 -16 -14 -13 15 16 18 30 1 -14 -5 10 21 28 29 14 3 -4 1 -11 14 13 -8 27 1 3 26 -2 -16 -4 1 -20 -15 28 24 28 -15 -8 27 -17 21 6 12 27 6 1 8 19 28 -12 -20 13 12 11 6 -8 15 20 29 -5 26 4 -13 -6 -18 2 -16 17 1 -2 -8 6 11 29 -9 -1 2 3 -9 -17 29 9 -11 -12 -7 -11 25 16 -5 19 -15 19 -11 23 29 7 -6 12 13 28 -17 -18 25 -18 11 15 -3 18 -8 -11 -4 18 5 20 29 14 -8 -15 24 5 -9 8 -14 18 20 -20 -2 26 15 11 3 -15 12 -1 -2 -11 19 10 8 -19 3 14 2 8 6 14 -2 -3 16 -19 0 9 -14 -13 -13 11 4 29 -1 8 3 28 28 8 22 0 -2 -2 -13 15 7 30 10 12 3 23 10 -19 -9 -6 -14 27 -4 26 -14 5 6 28 -11 23 15 28 -15 9 2 30 21 2 -2 12 -12 -18 27 -9 -2 -17 8 23 12 23 14 17 15 -2 -19 -19 18 -10 -5 19 5 28 -1 -5 -5 -6 0 -20 -9 -19 -3 10 28 15 -11 28 20 17 25 20 30 -17 -17 -20 16 12 -15 11 -19 28 22 21 -8 0 11 -14 -4 2 3 0 21 17 4 13 23 -7 -1 8 -14 -13 -8 24 4 18 27 25 -17 -5 -3 -18 14 -19 14 9 -7 0 -7 -20 -2 -2 -2 -10 19 -8 0 -4 1 13 6 15 30 9 28 13 29 3 16 19 6 1 16 19 -10 -18 -6 -18 -14 -20 1 25 -10 6 25 -19 -16 18 1 27 2 21 18 -19 -2 17 -10 -3 6 -3 12 -9 -7 20 -20 21 12 29 -7 -8 3 7 -8 14 28 22 -11 -11 14 -19 15 15 17 17 26 21 -4 -9 -3 -16 -9 -7 18 26 30 14 2 -14 -18 21 -19 1 8 18 1 2 13 -5 -6 -12 -1 11 19 25 1 9 17 22 6 -9 29 -18 23 6 29 -14 12 -1 -3 28 28 28 7 9 -10 -15 5 30 -8 12 -7 13 28 -10 4 5 24 -10 11 21 -7 26 29 4 4 6 -15 -6 -14 -5 19 -2 15 -14 25 11 3 -15 8 -10 30 7 -17 -11 24 -13 -9 8 11 28 3 -7 27 -10 30 0 8 22 8 29 -4 24 -17 3 -5 -17 -6 -5 0 -13 13 -20 5 -12 -14 -7 22 -10 3 23 -12 3 14 -6 3 -4 23 -6 10 -13 -8 23 29 4 -8 -14 -9 8 21 -20 2 22 6 -5 -2 15 -16 19 -19 26 -13 -20 -6 19 -15 2 -13 2 -12 -1 -8 17 26 23 -9 -13 21 23 -4 -20 0 -5 27 25 27 12 18 -19 -4 -7 27 26 -5 26 1 12 1 13 0 21 26 25 -5 -4 1 -18 25 9 30 -12 7 12 13 13 -8 -9 18 11 27 24 23 -1 22'
    challenge_data_proteome = 'EREVTSVKSSMNIMRAKTNGWFMMIVYMCDDSPFEKIREIRIDHIWCFVAICLHQEYYAQNWCCDWIGKDKYHHYDSECNSCMWIRHKSTFDLEHWFMFKIGFVNFMCVNHRCFGYRRSSYSMNDQCMRKFFQEQYDRENYCFAYQFACCFTKKRELQFFQDWELCMTYLFWSDMNTEPVQVQFKFPWGHVVCTGSKSVFHQWQAIHQIRPITFGVIWTDMTQWLKLRGNATYLDGHWTRFKNMWDVWQRMSQTPWRKEPRKCLGRDNAETRYQGWSFKCYPWPRRNGHPKGIQVLCHGHWPAIIRISASCLSPFLWGKQDVSDTLHWGRCQCIGEDQLRTPGKMVWCHTCVWGVDPWNFWMCKRGINGDVPFHMEMRIMRSYNCLIIVKACWPTNMEFQTENNKLQPRGCKHKMELKQSCRNAKKKLHNAITPCSLTSHNIYMSIFASSPEGTQCYEVNFNEMVDPRRGWISKCNQQCVEATKMYNWQTFGWNTSDILYPLFVWKNDAIAIAACMKSVCTETAYYFPYVAFHLYLCPVRQCPFCMRFQVECDGWGIGHGEVYWPVTTEWIEGSNYRRSEFRWKPHHYWQDVYFMWASSPWRMTQKPVLAAFIQFIGPHYKDDKQRYENCTHNSGAHHFNPKFFDRTTVMPSLMGIWMDWWDQLLWWKVQVTMMYQALMSAGSIDKANNPHDYTHFGHWAIRDDTCLICLHHRAEYYMSILEKEVNNFFKHNVCQPDVHFPGMRCEIIILCTCEKSLKTQNVVFQIIWQVFIMDVGFNITSRCTRTYAIGGPIHQCQDAFCGNLAQGDYTDGYDMLCHHRRRVENAEMCFHGVQPMILNNRPEEFVWMPKIYDLSLPYCILYQTWTECLRMGHFHTDMQEGERYQKYAENSKTWIPFHPRSKTDWFPLAEYEFCRYMTFLSKTLFVAGAVKFWCKANLDTENPQPAQCCIEYTEVMYGGFVWHTQWMSQVYFSGNKGKKRPCLPDQDPPHQNKFWFHTICISHGSVQCTHVHCSQGIWDRFIKCFNYFDPVLYIQDNGEMITNLQNMYMWPADEFHAIIWMQPWSFMDEMCVCSYSMCTMEGVQTNHTDTCCICEEVRKNIQAYCDPFDSVYWITTSQMTGWRTQTDMALASIDPKNTPVYIWGWHYFQEVCSYQTNPNRTKKACDRCFWGENPWMFWRAHPNMDQRGDTNQHGRSIHGHSLSWMSHPFWCNLPWWLNAYFMRAPNPYQAPCSVGMWGSIHSLTLVRHNWYFDMYEGQFIEWRIKSADDAQQFMVWPIYNSKEDHCVEDRKAQKLAQCVDNLKGCICQSWENIRKTCFYRTRWSYVCWYILMQTCCEHDNMCNKVTNDGFACVTYHWNMKPLYNTMPYHLNGMTYENDGWTWCPNMELFRCYQMNSHMRGCYILCCFINGPDNRLHESPHYGGMCCDSREFAQQIWHGDDLLWLFRGWARKMCRMWSSGKCHVVNKMALGSYTISRTKYIYIQTYETPIGAMFWIGNYKIWATEMDSLWLKCRETNTEFALDVCIGPMANYPGRQPVHFNKLQPWVPTPWEIIERSYMSEPKHLKCDLSDELKWDWMKNMRTAISRSDFHCGVVEYCAKESANVYPMTYCYDGTKCGFICADHCNRLVQMLWEWNWYEIYEIPTFLCQNTEWFATGIIKERCNLWHCDHTTFSCRVHVFWQWLHIATENHRHRKVARLCPVLGRWITYQTPVHGKCRNMTEDDGDNQADPWYGLSMYNVLDHPSLLAPFINPRRIRWVKPLIPHKYGQCQRWDRVRRVDLHLPCICSYDPYTRFIRKHSGTHQRHQGMHPSQQPMTIYMSDDHPWMHYISMSQWYECPAPVHKPWKTCGFEMYTCAAFGPFYLKKGKMRCRPEYMVVWPMWEKNCASVSQNGHDSHQHRTRPFRRDFEWVTCAYAICRCERCPTHYYCANSKGWWMHKALCDVMAWPVEAKCYHFKFYCKFDGYNVYFRSVYMLGKNMGKISADTQAYSIGRCFHVHLTLRSALFHKDYQVVQSLLSMELLDHRRGIHVIIAGTTQGGTKFCMSSQRIPYATPDWTWCSYCCKCRKPGQSIMAEDRMWRKPVDRGDFIPPMYDMIALLWTEMWSSKYAGMEWHNGTFEDEDDRRWDHFQWNIAYTWRLFCQGLTHLKIPCWYMGNELFTICSFRVHVNETEDHNHTYAGRVFMRIKLSCDCSEPFRIQGTKIIHIEYECKFWMIHHDRYLNPTWALVEWFCLCSGYQYWYQNGMTPTAQPCQPGNKIWVMEFRKPMKFKTEIAAVCMNELHLIFSRMSIDAKAVYEKNTPNLHEPDQKVTRCQCSSAPVNEWQCDIMLQSDEHIRQVDHVKCFVWTMWKFTWILTGFVTIRRDFSYSGWNTLLGYDSGRWFSAPMRMHYILKAHPKQQQRFCGWMWQEQDSGLGLKWHFSMYLNGYVPWTETWQSCVSQVTAVCRIATMLCWRLHKSEGRVFMCFYVLECYCATMYIQKVLGSHPRVVVSANCCMFHIPMYHIVPKQMEKYMWSSGKHRDCPLLCMRNAHGETSKFWVEENHAETPAAVCKPVIMGFRMDPTKRGQAGGWMGYDTGKDARAVMDPFIPPDYKENLNYRCSMYPFPKQMHCLGNYVCMCVTACVANYISTHMNDGTQAFAGYASRKHQWATRKLYLHVGIDMCLFEFDKHACTRMQGWYDGSEKLLTYQDPNLWEGSEFPCTTTDVSGYIKPEFVKHDPAWDHIDKDWPIGKYLVWWWSLTKFWWGHHQKKYYSCAFQEKHCWARRIKEFKADQHRTWHRCQRSCDREITRGVIMPTEMTWLMYCNWMAIDEMWFHTMPNYKLDSNKWTDTNGKRWHVREMMHIPWSRMFCAPAICKAKFSWTPEAYTGHTEMVTIVQINGINVDICANLPVHPKANDYGTESTEVVTSKTWQKHMFAYFGSRHMRIVFQWFHVSYELAFPANIWKGWLTRDWHHIMAQSMWIKIGNMADVALHQEQASHNCMAYFWMCWMLWWEQCLLVWIIPDCFLRWFLYNRRYEHDGPIWSFSVPSSIRHCKIMNPAPVRLHWHAYGHLPFHGHRKISVAQSTCSPGFMEFYKTESCFTNIVEKVHGWTWDEECDWHAKGIMYVNWTQWWEMHRMFKTFFLAAKLRKLPVCSESQIWASYNYVQSSLHILLAQWEPNPLKPWMWAPPLKQDHWKMDVTNETSHFHTANPKQAEAYNKLHQPTHVQKHLQDLGVMYAQLMNMEMQEHRQCHTCYCEAWQVQIGGRYCKRKTVAEEYCMKCNCCYREHKQTSVGWNQEPMVYYWALWHHTDLREQAWEERILKRQGVCIKIVMEFEKDMAWPDVMDNASCLYYKTRPTKNLAQCGWTFICVWACCCFVECAYIWEHIKEEGAEDFMEITFEKDFCGQWTKRMSIYWHRDGQSLWARFREADKLQWVNQNFPNIMPAGPNYASYYWSYPGWCFIHKEQGWYIMIDLHMCMAWLWDTGRLIFHCTAWSAFVFGYQEQGYDFCPIWPLLIHQDNHSPKYHFEGGTHPWARIKTRNHFLSQKRNEFRPAIRHCDVVWNAFGEWASWWELVEAMTPNEGWYFKATYDFAQVKRCPVGNEFIMVNSHTKLQKWWLSLELDFTTKELHVYYPYHSSESTRCKKTFAVCPYENVTSAGHETYQNAGWWKSEAAKCHWWNAYTSAKSMSRNNCMHYTAECMWTYALWCSGGTLQESDKNKRRHKFSMTQQGWRQCEVNHVYLPYVGEMWMKEDAWGDNQYPSQQKNTKYEWQYCCLNCFMQSNVSAPKLNEIEFVEEIHKKLFYLMYQCQATYMFYVCYYMIKMEFDTANGYQAYVVNTCIRDRWMVPRHCCYIRTASREEAEAKIMQPNPKHLWHESLPIMLFMNHTKVMFLLIRRSVKNDITDCAHWVMIPKSVQQKKPGDLNSCFAGAHPPYEMVLIKIWYEVMMCEREFVPDCSGPHMRRCPRADCHICPDMYRVCTVIAKDADHCWWVCYRYHPFPWYHEMYPVSGLRTFGRWDNTCYNNFCACMFQPYPIYMKLGWTDPELITVRAYVEHTRQNRNPCICCASIAMPMCGSFNHHTSLEERCQGHYCYDISQRSAPARTAHFTDETLCVDKWNHIWNSSCMHNLYPNLGPYTGFAKVMKWPEQWTPQNMWYEFRFPDVGDHAFSKMHATWWTDRTLLINENCSFVAMKMANEHKSPFTYYAFSVMHHIHFKNDDVEIFMSWCEVQLHAYTWFNEFCWSYFMGTNHMHQKLRCFQRQLDMCMVWCAQRYTTPQMKACHPCINMIIKWDNLTHQLHGPIYPWIQKQWQQHYFVSNKPEPERKWTNFLAYAETEEFYPTKHPPVVSEAVDSKNQPTADYNGQDSGNHRCFDMWMDVRVIGCLYVITDMFWNNLRHWEKHCLVQMPGAVVNRRYERKSWQRFQQQIACRINGALLAHTAAYAPWSIRVFAADHQGMTREEYCLQGEVITRVPFHLTTQNPNTVNKFWWWVLVWCERERIRTKKSIRWFHALVGPFRSVEKNITGASWVKIWVRFFAFMASLDKSCHFHQWRDGPCDMHHPICPVIHHGELMYGYFPSNKSAGRHWWHQNCSLIAGQFRSVSMGWRDLATEIPSQDMNAPEFHWFECNFHRQTMMVKFTVHFNTPQWHGLFGQVKMFEDEKMWWLWQKWGEVNLWMEQQHQEWNLIFPPVYWEQQVFHSGAMSPDVLMMAMDGIFADVIVMEVYEVYMCDDRIDSRIDCTHIDDSPPPCALWVLWYMMKNYEKSDPGEPPAPLRWSIDWSMELHVEMEIEFTSNTNGRGWPPKQGLYGDCYMLQFLMPINYFIYYRWRIGHCMMQAQYLPWCTNIHYSWDWFDRMYYGYPSCEFMSNKEKHHATFTHHHFTLIVLYAWGRVQFTHVGFEYDYCTMTFSNCDAEGGKVVLVVLAFCAYRFFRGGQEEFVLQFWDKCIVTKMSRFGQYSWKTCLQHLEAKEHAASEGMQRDYPNTETVIEKAFLHGMYCFASKYGREIKWAYCYFFCGG'
    
    print peptide_identification(challenge_data_vector,challenge_data_proteome)
