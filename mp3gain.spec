%define name mp3gain
%define release 2
%define version 1.5.2
%define tarball_version 1_5_2_r2

Name:		%name
Version:	%version
Release:	%release
Summary:	Lossless MP3 volume adjustment tool

Group:		Sound
License:	LGPL
URL:		https://mp3gain.sourceforge.net
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


%changelog
* Sat Aug 07 2010 Ahmad Samir <ahmadsamir@mandriva.org> 1.5.2-1mdv2011.0
+ Revision: 567270
- update to 1.5.2
- unpack the patches
- rediff patches 0,2
- drop patch1, fixed upstream
- drop patch3, not needed any more

* Mon May 18 2009 Jérôme Brenier <incubusss@mandriva.org> 1.4.6-4mdv2010.0
+ Revision: 377397
- add a patch to fix str fmt

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 1.4.6-3mdv2009.0
+ Revision: 252943
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.4.6-1mdv2008.1
+ Revision: 136608
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat May 05 2007 Lenny Cartier <lenny@mandriva.org> 1.4.6-1mdv2008.0
+ Revision: 22608
- Import mp3gain




* Fri May 04 2007 Lenny Cartier <lenny@mandriva.com> 1.4.6-1mdv2008.0
- stole rpm from fedora

* Tue Nov 28 2006 Brian Pepple <bpepple@fedoraproject.org> - 1.4.6-4
- Bump.

* Sun Nov 26 2006 Brian Pepple <bpepple@fedoraproject.org> - 1.4.6-3
- D'Oh! Add HAVE_MEMCPY back to cflag patch.

* Sun Nov 26 2006 Brian Pepple <bpepple@fedoraproject.org> - 1.4.6-2
- Update cflags patch to use RPM_OPT_FLAGS.

* Mon Nov 20 2006 Brian Pepple <bpepple@fedoraproject.org> - 1.4.6-1
- Initial Livna spec.
