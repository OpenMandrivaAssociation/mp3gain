%define name mp3gain
%define release %mkrel 1
%define version 1.4.6
%define tarball_version 1_4_6

Name:		%name
Version:	%version
Release:	%release
Summary:	Lossless MP3 volume adjustment tool

Group:		Sound
License:	LGPL
URL:		http://mp3gain.sourceforge.net
Source0:	http://osdn.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{tarball_version}-src.tar.bz2
Source1:	%{name}.1.bz2
Source2:	README.method
Patch0:		mp3gain_tempfile_default.patch.bz2
Patch1:		mp3gain_exit.patch.bz2
Patch2:		mp3gain_cflags.patch.bz2
	

%description
MP3Gain analyzes and adjusts mp3 files so that they have the same
volume. It does not just do peak normalization, as many normalizers
do. Instead, it does some statistical analysis to determine how loud
the file actually sounds to the human ear. Also, the changes MP3Gain
makes are completely lossless. There is no quality lost in the change
because the program adjusts the mp3 file directly, without decoding
and re-encoding.


%prep
%setup -q -n %{name}-%{tarball_version}-src
%patch0 -p1 -b .tempfile
%patch1 -p1 -b .exit
%patch2 -p1 -b .cflags
install -p -m 644 %{SOURCE2} .
%{__sed} -i 's/\r//' lgpl.txt


%build
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
install -Dp -m 755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -Dp -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1.bz2


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc lgpl.txt README.method
%{_bindir}/%{name}
%{_mandir}/man1/*
