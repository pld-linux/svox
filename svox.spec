Summary:	SVOX Pico software speech synthesizer engine
Summary(pl.UTF-8):	Silnik programowego syntezatora mowy SVOX Pico
Name:		svox
%define	subver	git20110131
Version:	1.0
Release:	0.%{subver}.1
License:	Apache v2.0
Group:		Libraries
# originally http://android.git.kernel.org/?p=platform/external/svox.git;a=summary
Source0:	http://ftp.de.debian.org/debian/pool/non-free/s/svox/%{name}_%{version}+%{subver}.orig.tar.gz
# Source0-md5:	e9dd590721705c50ee5d7f262bd3c697
Patch0:		0001-autoconf-building-of-library-using-libtool.patch
Patch1:		0002-gitignore-for-autotools-files.patch
Patch2:		0003-pico2wave-Convert-text-to-.wav-using-svox-text-to-sp.patch
Patch3:		0004-add-header-files.patch
Patch4:		0005-Install-lang-files.patch
Patch5:		0006-Set-picolangdir.patch
Patch6:		0008-64bits.patch
Patch7:		%{name}-link.patch
URL:		http://www.android.com/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	libtool >= 2:2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The SVOX Pico engine is a software speech synthesizer for German,
English (GB and US), Spanish, French and Italian.

SVOX produces a clear and distinct speech output made possible by the
use of Hidden Markov Model (HMM) algorithms.

%description -l pl.UTF-8
Silnik SVOX Pico to programowy syntezator mowy dla języka
niemieckiego, angielskiego (brytyjskiego i amerykańskiego),
hiszpańskiego, francuskiego i włoskiego.

SVOX wytwarza czystą i wyraźną mowę dzięki użyciu algorytmów opartych
na ukrytych modelach Markowa (HMM - Hidden Markov Model).

%package devel
Summary:	Header files for SVOX Pico TTS library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki SVOX Pico TTS
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for SVOX Pico TTS library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki SVOX Pico TTS.

%package static
Summary:	Static SVOX Pico TTS library
Summary(pl.UTF-8):	Statyczna biblioteka SVOX Pico TTS
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static SVOX Pico TTS library.

%description static -l pl.UTF-8
Statyczna biblioteka SVOX Pico TTS.

%package lang-de
Summary:	SVOX Pico TTS language files (lingware) for German
Summary(pl.UTF-8):	Pliki językowe (lingware) syntezatora SVOX Pico dla języka niemieckiego
Group:		Applications/Text
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description lang-de
SVOX Pico TTS language files (lingware) for German.

%description lang-de -l pl.UTF-8
Pliki językowe (lingware) syntezatora SVOX Pico dla języka
niemieckiego.

%package lang-en_GB
Summary:	SVOX Pico TTS language files (lingware) for UK English
Summary(pl.UTF-8):	Pliki językowe (lingware) syntezatora SVOX Pico dla angielskiego brytyjskiego
Group:		Applications/Text
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description lang-en_GB
SVOX Pico TTS language files (lingware) for UK English.

%description lang-en_GB -l pl.UTF-8
Pliki językowe (lingware) syntezatora SVOX Pico dla języka
angielskiego brytyjskiego.

%package lang-en_US
Summary:	SVOX Pico TTS language files (lingware) for US English
Summary(pl.UTF-8):	Pliki językowe (lingware) syntezatora SVOX Pico dla angielskiego amerykańskiego
Group:		Applications/Text
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description lang-en_US
SVOX Pico TTS language files (lingware) for US English.

%description lang-en_US -l pl.UTF-8
Pliki językowe (lingware) syntezatora SVOX Pico dla języka
angielskiego amerykańskiego.

%package lang-es
Summary:	SVOX Pico TTS language files (lingware) for Spanish
Summary(pl.UTF-8):	Pliki językowe (lingware) syntezatora SVOX Pico dla języka hiszpańskiego
Group:		Applications/Text
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description lang-es
SVOX Pico TTS language files (lingware) for Spanish

%description lang-es -l pl.UTF-8
Pliki językowe (lingware) syntezatora SVOX Pico dla języka
hiszpańskiego.

%package lang-fr
Summary:	SVOX Pico TTS language files (lingware) for French
Summary(pl.UTF-8):	Pliki językowe (lingware) syntezatora SVOX Pico dla języka francuskiego
Group:		Applications/Text
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description lang-fr
SVOX Pico TTS language files (lingware) for French.

%description lang-fr -l pl.UTF-8
Pliki językowe (lingware) syntezatora SVOX Pico dla języka
francuskiego.

%package lang-it
Summary:	SVOX Pico TTS language files (lingware) for Italian
Summary(pl.UTF-8):	Pliki językowe (lingware) syntezatora SVOX Pico dla języka włoskiego
Group:		Applications/Text
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description lang-it
SVOX Pico TTS language files (lingware) for Italian.

%description lang-it -l pl.UTF-8
Pliki językowe (lingware) syntezatora SVOX Pico dla języka
włoskiego.

%package docs
Summary:	SVOX Pico TTS engine documentation
Summary(pl.UTF-8):	Dokumentacja silnika syntezy mowy SVOX Pico
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description docs
SVOX Pico TTS engine documentation.

%description docs -l pl.UTF-8
Dokumentacja silnika syntezy mowy SVOX Pico.

%prep
%setup -q -n %{name}-%{version}+%{subver}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
cd pico
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C pico install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pico2wave
%attr(755,root,root) %{_libdir}/libttspico.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libttspico.so.0
%dir %{_datadir}/pico
%dir %{_datadir}/pico/lang

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libttspico.so
%{_libdir}/libttspico.la
%{_includedir}/pico*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libttspico.a

%files lang-de
%defattr(644,root,root,755)
%{_datadir}/pico/lang/de-DE_*.bin

%files lang-en_GB
%defattr(644,root,root,755)
%{_datadir}/pico/lang/en-GB_*.bin

%files lang-en_US
%defattr(644,root,root,755)
%{_datadir}/pico/lang/en-US_*.bin

%files lang-es
%defattr(644,root,root,755)
%{_datadir}/pico/lang/es-ES_*.bin

%files lang-fr
%defattr(644,root,root,755)
%{_datadir}/pico/lang/fr-FR_*.bin

%files lang-it
%defattr(644,root,root,755)
%{_datadir}/pico/lang/it-IT_*.bin

%files docs
%defattr(644,root,root,755)
%doc pico_resources/docs/SVOX_Pico_{Lingware,Manual,architecture_and_design}.pdf
