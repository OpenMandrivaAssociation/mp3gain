%define name mp3gain
%define release %mkrel 1
%define version 1.5.2
%define tarball_version 1_5_2_r2

Name:		%name
Version:	%version
Release:	%release
Summary:	Lossless MP3 volume adjustment tool

Group:		Sound
License:	LGPLv2+
URL:		http://mp3gain.sourceforge.net
Source0:	http://osdn.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{tarball_version}-src.zip
Source1:	%{name}.1.bz2
Source2:	README.method
Patch0:		mp3gain_tempfile_default.patch
Patch2:		mp3gain_cflags.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
	

%description
MP3Gain analyzes and adjusts mp3 files so that they have the same
volume. It does not just do peak normalization, as many normalizers
do. Instead, it does some statistical analysis to determine how loud
the file actually sounds to the human ear. Also, the changes MP3Gain
makes are completely lossless. There is no quality lost in the change
because the program adjusts the mp3 file directly, without decoding
and re-encoding.


%prep
%setup -q -c %{name}-%{tarball_version}-src
%patch0 -p1 -b .tempfile
%patch2 -p1 -b .cflags
install -p -m 644 %{SOURCE2} .
%{__sed} -i 's/\r//' lgpl.txt


%build
%make


%install
rm -rf %{buildroot}
install -Dp -m 755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dp -m 644 %{SOURCE1} %{buildroot}%{_mandir}/man1/%{name}.1.bz2


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc lgpl.txt README.method
%{_bindir}/%{name}
%{_mandir}/man1/*
