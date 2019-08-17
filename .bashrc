# .bashrc

# User specific aliases and functions

if [ -f /etc/bashrc ]; then
      . /etc/bashrc   # --> Read /etc/bashrc, if present.
fi

# various aliases
alias dsk="cd ~/Desktop"
alias dev="cd ~/Development"
alias home="cd ~"
alias mute="osascript -e 'set Volume 0'"
alias turnup="osascript -e 'set Volume 10'"
alias chrome='open "/Applications/Google Chrome.app"'
alias spotify="open /Applications/Spotify.app"
alias lock='pmset displaysleepnow'
alias weather='python3 /Users/thomashayes/Development/python/automation/weather_notf.py'
alias dk="bash /Users/thomashayes/Development/python/data_science/sportsDataAnalysis/lineupOptimizer/mlb/run_mlb_scripts.sh" 
alias jup="jupyter notebook --notebook-dir=."

# ---------------------------------- # 
#  functions to allow user input
# ---------------------------------- # 

# make and go to dir
mkdirg ()
{
	mkdir -p $1
	cd $1
}

# go up 'x' amount of dir
up ()
{
	local d=""
	limit=$1
	for ((i=1 ; i <= limit ; i++))
		do
			d=$d/..
		done
	d=$(echo $d | sed 's/^\///')
	if [ -z "$d" ]; then
		d=..
	fi
	cd $d
}

# convert .ipynb to .py
jyp ()
{

    jupyter nbconvert --to script $1

}




# shell appearance stuff 
export PS1="\[\033[36m\]\u\[\033[m\]@\[\033[32m\]\h:$ "
export CLICOLOR=1
export LSCOLORS=ExFxBxDxCxegedabagacad

# PATH=$PATH:/home/username/bin:/usr/local/homebrew
# export PATH
