\ProvidesClass{mfa}
\LoadClass{article}

%% Sheet counter
\newcounter{sheetno}
\newcommand*{\sheet}[1]{\setcounter{sheetno}{#1}}

%% packages
\RequirePackage[utf8]{inputenc}
\RequirePackage{lmodern, array, amsmath, amsthm, amssymb, microtype,
IEEEtrantools, titlesec, titling, mathptmx, mathtools}
\RequirePackage[dvipsnames]{xcolor}
\RequirePackage[ngerman]{babel}
\RequirePackage[pdfencoding=unicode, psdextra]{hyperref}

\fontfamily{ptm}\selectfont

%% Heading formats
\titleformat{\section}[hang]{\bf}{Aufgabe \arabic{sheetno}.\arabic{section}}{1em}{}[]
\titleformat{\subsection}[hang]{\bf}{(\arabic{subsection})}{1em}{}[]


%% operators
\DeclareMathOperator*{\argmax}{arg\,max}
\DeclareMathOperator*{\argmin}{arg\,min}

%% At begin document, do this
\AtBeginDocument{
   %% Metadata
   \author{Rasmus Diederichsen \and Laura Goerke \and Tim Brockmeyer \and Katharina
   Filodda}
   \date{\today}
   \title{Mathematik für Anwender II --- Blatt \arabic{sheetno}}
   \hypersetup{
      pdftitle          = {\thetitle},
      pdfauthor         = {\theauthor},
   }
}

%% Misc commands
\newcommand{\mbf}[1]{\mathbf{#1}}

\setlength{\parindent}{0pt}

\newcommand{\inlinepmatrix}[1]{\begin{pmatrix}#1\end{pmatrix}}

