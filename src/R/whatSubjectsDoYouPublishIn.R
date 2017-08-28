########################################
#For a given author, what subjects in their
#pubmed articles have they published in?
#
#Kind of rough around the edges...but pretty cool still!
########################################

library(RISmed)
library(tm)
library(SnowballC)
library(wordcloud)

terms<-c(
         "Tatonetti[AU] AND Columbia[Affiliation]", 
         "Hripcsak[AU] AND Columbia[Affiliation]"
        )

mesh<-NULL
titles <- NULL
abstracts <- NULL

for(i in 1:length( terms ) ){
  
  author <- terms[i]
  minyear <- 2012
  maxyear <- 2018
  search_query <- EUtilsSummary( author, 
                                 mindate=minyear, 
                                 maxdate=maxyear )
  
  records<- EUtilsGet( search_query ) 
  
  list <- Mesh(records)
  
  strs <-   unlist(
        sapply(Mesh(records),function(x){
        if(is.factor(x[[1]])){
          vec <- as.character(x[[1]])
          }
        }
      )
    )
    
  mesh[[i]] <-  strs
  
  titles[[i]] <- ArticleTitle(records)
  
  abstracts[[i]] <- AbstractText(records)
  
  docs <- Corpus( VectorSource( AbstractText(records) ) )
  
  docs <-tm_map(docs,content_transformer(tolower))
  
  #remove punctuation
  # docs <- tm_map(docs, removePunctuation)
  # #Strip digits
  # docs <- tm_map(docs, removeNumbers)
  # #remove stopwords
  docs <- tm_map(docs, removeWords, stopwords("english"))
  # #remove whitespace
  # docs <- tm_map(docs, stripWhitespace)
  # #Stem document
  docs <- tm_map(docs,stemDocument)

  myStopwords <- c("can", "say","one","way","use",
                    "also","howev","tell","will",
                    "much","need","take","tend","even",
                    "like","particular","rather","said",
                    "get","well","make","ask","come","end",
                    "first","two","help","often","may",
                    "might","see","someth","thing","point",
                    "post","look","right","now","think","‘ve ",
                    "‘re ","anoth","put","set","new","good",
                    "want","sure","kind","larg","yes,","day","etc",
                    "quit","sinc","attempt","lack","seen","awar",
                    "littl","ever","moreov","though","found","abl",
                    "enough","far","earli","away","achiev","draw",
                    "last","never","brief","bit","entir","brief",
                    "great","lot","report","effect","significant",
                   "severe")
  docs <- tm_map(docs, removeWords, myStopwords)
  
  dtm <- DocumentTermMatrix(docs)
  #convert rownames to filenames
  rownames(dtm) <- ArticleTitle(records)
  #collapse matrix by summing over columns
  freq <- colSums(as.matrix(dtm))
  #length should be total number of terms
  length(freq)
  #create sort order (descending)
  ord <- order(freq,decreasing=TRUE)
  #List all terms in decreasing order of freq
  cat( terms[i],":\n")
  cat( head(names(freq[ord])) , "\n")
  cat( head(freq[ord]) , "\n")
  
  
  wordcloud(docs, max.words = 20, 
                  random.order = FALSE,colors=brewer.pal(8, "Dark2"),
                  main=terms[i])

  
  }




