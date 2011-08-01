" System vimrc file for MacVim
"
" Maintainer:	Bjorn Winckler <bjorn.winckler@gmail.com>
" Last Change:	Sat Aug 29 2009

set nocompatible

" The default for 'backspace' is very confusing to new users, so change it to a
" more sensible value.  Add "set backspace&" to your ~/.vimrc to reset it.
set backspace+=indent,eol,start

" Disable localized menus for now since only some items are translated (e.g.
" the entire MacVim menu is set up in a nib file which currently only is
" translated to English).
set langmenu=none

""""""""""""""""""""""""""""""""""""
" Mak's Vim settings		   "
""""""""""""""""""""""""""""""""""""
" File Types
filetype on
filetype plugin on
syntax on 

" Line number
set number

" Fonts
set guifont=monofur:h14

" Key Maps for NERDTree
nmap <F2> :NERDTree <CR>
nmap <F3> :NERDTreeClose <CR>

" Vim width and height
set lines=50 columns=150

" Cancel swap files
set nobackup
set nowb
set noswapfile

" Tabs setting
set expandtab
set tabstop=4
set shiftwidth=4
set softtabstop=4

" Encoding
set encoding=utf-8
set fileencoding=utf-8

" Hightlight search
set hlsearch

" Cancel toolbar
set guioptions-=T

let g:SuperTabDefaultCompletionType = "context"


