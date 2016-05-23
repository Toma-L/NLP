library(XML)
fileUrl <- "file:///Users/thomas/Documents/R%20Files/messages.htm"
doc <- htmlTreeParse(fileUrl, useInternal = TRUE)
users <- xpathSApply(doc, "//span[@class='user']", xmlValue)
meta <- xpathSApply(doc, "//span[@class='meta']", xmlValue)
p <- xpathSApply(doc, "//p", xmlValue)

Ku <- 0
for(i in 1:NROW(p[users == "Ku Chou"])) {
        Ku[i] <- p[users == "Ku Chou"][i]
}
nch <- nchar(Ku)
mean(nchar(Ku), trim = .1)

Thomas <- 0
for(i in 1:NROW(p[users == "Thomas Lin"])) {
        Thomas[i] <- p[users == "Thomas Lin"][i]
}
Thomas
mean(nchar(Thomas), trim = .05)
Xie
NROW(Xie)
mean(nchar(Xie), trim = .1)

unique(users)
tab <- table(users)
tabdf <- data.frame(Name = rownames(tab), MSG = tab)
tabdf <- tabdf[, -2]
dim(tabdf)
tabdf <- tabdf[order(tabdf$MSG, decreasing = TRUE), ]
head(tabdf, 103)
rownames(tabdf) <- 1:NROW(tabdf[, 2])

NROW(meta[str_detect(meta, "2013")])
